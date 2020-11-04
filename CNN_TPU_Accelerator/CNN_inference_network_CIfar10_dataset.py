import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim
import torch.utils.data
import torch.nn.functional as F
from torch.autograd import Variable
import distiller.quantization as quantization
from distiller.apputils.checkpoint import load_checkpoint
import torchvision
import torchvision.transforms as transforms
import numpy
from bitstring import BitArray

import math
from torch.nn.parameter import Parameter
from torch.nn.modules.utils import _pair
import torch.autograd.function as Function

###############################################

import math
import torch
from torch.nn.parameter import Parameter
from torch.nn import functional as F
from torch.nn import init
from torch._ops import ops
from torch.nn.modules.module import Module
from torch.nn.modules.utils import _single, _pair, _triple
#from torch.nn.intrinsic import ConvReLU2d
from torch._jit_internal import List

#from ..._jit_internal import List
#from caffe2.python.schema import List


# torch.device('cpu')

########################################  Pre-Processing Cifar 10 ###############################

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


##############################  Test 2 ################################

#####################################################################################################

class _ConvNd(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1,
                 padding=0, dilation=1, groups=1, bias=True,
                 padding_mode='zeros'):
        super(_ConvNd, self).__init__()
        if padding_mode != 'zeros':
            raise NotImplementedError(
                "Currently only zero-padding is supported by quantized conv")
        if in_channels % groups != 0:
            raise ValueError('in_channels must be divisible by groups')
        if out_channels % groups != 0:
            raise ValueError('out_channels must be divisible by groups')
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.transposed = False
        self.output_padding = 0
        self.groups = groups
        self.padding_mode = padding_mode
        # Initialize as NCHW. set_weight will internally transpose to NHWC.
        qweight = torch._empty_affine_quantized(
            [out_channels, in_channels // self.groups] + list(kernel_size),
            scale=1, zero_point=0, dtype=torch.qint8)
        bias_float = (
            torch.zeros(out_channels, dtype=torch.float) if bias else None)

        self.set_weight_bias(qweight, bias_float)
        self.scale = 1.0
        self.zero_point = 0

    def extra_repr(self):
        s = ('{in_channels}, {out_channels}, kernel_size={kernel_size}'
             ', stride={stride}, scale={scale}, zero_point={zero_point}')
        if self.padding != (0,) * len(self.padding):
            s += ', padding={padding}'
        if self.dilation != (1,) * len(self.dilation):
            s += ', dilation={dilation}'
        if self.groups != 1:
            s += ', groups={groups}'
        if self.bias() is None:
            s += ', bias=False'
        return s.format(**self.__dict__)

    # ===== Serialization methods =====
    # The special consideration here is that we have to unpack the weights into
    # their regular QTensor form for serialization. Packed weights should not
    # live outside the process in which they were created, rather they should be
    # derived from the QTensor weight.
    def _save_to_state_dict(self, destination, prefix, keep_vars):
        super(_ConvNd, self)._save_to_state_dict(destination, prefix, keep_vars)
        (w, b) = self._weight_bias()
        destination[prefix + 'weight'] = w
        destination[prefix + 'scale'] = torch.tensor(self.scale)
        destination[prefix + 'zero_point'] = torch.tensor(self.zero_point)
        destination[prefix + 'bias'] = b

    @torch.jit.export
    def __getstate__(self):
        if not torch.jit.is_scripting():
            raise RuntimeError(
                'torch.save() is not currently supported for quantized modules.'
                ' See https://github.com/pytorch/pytorch/issues/24045.'
                ' Please use state_dict or torch.jit serialization.')
        (w, b) = self._weight_bias()
        return (
            self.in_channels,
            self.out_channels,
            self.kernel_size,
            self.stride,
            self.padding,
            self.dilation,
            self.transposed,
            self.output_padding,
            self.groups,
            self.padding_mode,
            w,
            b,
            self.scale,
            self.zero_point,
            self.training
        )

    # ===== Deserialization methods =====
    # Counterpart to the serialization methods, we must pack the serialized
    # QTensor weight into its packed format for use by the FBGEMM ops.
    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict,
                              missing_keys, unexpected_keys, error_msgs):
        self.set_weight_bias(
            state_dict[prefix + 'weight'], state_dict[prefix + 'bias'])
        state_dict.pop(prefix + 'weight')
        state_dict.pop(prefix + 'bias')
        self.scale = float(state_dict[prefix + 'scale'])
        state_dict.pop(prefix + 'scale')
        self.zero_point = int(state_dict[prefix + 'zero_point'])
        state_dict.pop(prefix + 'zero_point')
        super(_ConvNd, self)._load_from_state_dict(
            state_dict, prefix, local_metadata, False, missing_keys,
            unexpected_keys, error_msgs)

    @torch.jit.export
    def __setstate__(self, state):
        self.in_channels = state[0]
        self.out_channels = state[1]
        self.kernel_size = state[2]
        self.stride = state[3]
        self.padding = state[4]
        self.dilation = state[5]
        self.transposed = state[6]
        self.output_padding = state[7]
        self.groups = state[8]
        self.padding_mode = state[9]
        self.set_weight_bias(state[10], state[11])
        self.scale = state[12]
        self.zero_point = state[13]
        self.training = state[14]

######################################

class Conv2d(_ConvNd):

    _FLOAT_MODULE = nn.Conv2d

    def __init__(self, in_channels, out_channels, kernel_size, stride=1,
                 padding=0, dilation=1, groups=1, bias=True,
                 padding_mode='zeros'):
        kernel_size = _pair(kernel_size)
        stride = _pair(stride)
        padding = _pair(padding)
        dilation = _pair(dilation)
        super(Conv2d, self).__init__(
            in_channels, out_channels, kernel_size, stride, padding, dilation,
            groups, bias, padding_mode)

    def _get_name(self):
        return 'QuantizedConv2d'

    def set_weight_bias(self, w, b):
        # type: #(torch.Tensor, Optional[torch.Tensor]) -> None
        self._packed_params = torch.ops.quantized.conv2d_prepack(
            w, b, self.stride, self.padding, self.dilation, self.groups)

    def _weight_bias(self):
        return torch.ops.quantized.conv2d_unpack(self._packed_params)

    def weight(self):
        (w, _) = torch.ops.quantized.conv2d_unpack(self._packed_params)
        return w

    def bias(self):
        (_, b) = torch.ops.quantized.conv2d_unpack(self._packed_params)
        return b

    def forward(self, input):
        # Temporarily using len(shape) instead of ndim due to JIT issue
        # https://github.com/pytorch/pytorch/issues/23890
        if len(input.shape) != 4:
            raise ValueError("Input shape must be `(N, C, H, W)`!")
        return ops.quantized.conv2d(
            input, self._packed_params, self.stride, self.padding,
            self.dilation, self.groups, self.scale, self.zero_point)

    # @classmethod
    # def from_float(cls, mod):
    #     r"""Creates a quantized module from a float module or qparams_dict.
    #     Args:
    #         mod (Module): a float module, either produced by torch.quantization
    #           utilities or provided by the user
    #     """
    #     if hasattr(mod, 'weight_fake_quant'):
    #         # assert type(mod) == cls.__QAT_MODULE, ' nnq.' + cls.__name__ + \
    #         # '.from_float only works for ' + cls.__QAT_MODULE.__name__
    #         if type(mod) == nniqat.ConvBn2d:
    #             mod.weight, mod.bias = fuse_conv_bn_weights(
    #                 mod.weight, mod.bias, mod.running_mean, mod.running_var,
    #                 mod.eps, mod.gamma, mod.beta)
    #         assert hasattr(mod, 'activation_post_process'), \
    #             'Input QAT module must have observer attached'
    #         weight_post_process = mod.weight_fake_quant
    #         activation_post_process = mod.activation_post_process
    #     else:
    #         assert type(mod) == cls._FLOAT_MODULE, \
    #             ' nnq.' + cls.__name__ + '.from_float only works for ' + \
    #             cls._FLOAT_MODULE.__name__
    #         assert hasattr(mod, 'qconfig'), \
    #             'Input float module must have qconfig defined.'
    #         # workaround for sequential, ConvReLU2d should probably
    #         # inherit from Conv2d instead
    #         if type(mod) == nni.ConvReLU2d:
    #             activation_post_process = mod[1].activation_post_process
    #             mod = mod[0]
    #         else:
    #             activation_post_process = mod.activation_post_process
    #         weight_post_process = mod.qconfig.weight()
    #         weight_post_process(mod.weight)
    #     act_scale, act_zp = activation_post_process.calculate_qparams()
    #     assert weight_post_process.dtype == torch.qint8, \
    #         'Weight observer must have a dtype of qint8'
    #     qweight = _quantize_weight(mod.weight.float(), weight_post_process)
    #     qconv = cls(mod.in_channels, mod.out_channels, mod.kernel_size,
    #                 mod.stride, mod.padding, mod.dilation, mod.groups,
    #                 mod.bias is not None, mod.padding_mode)
    #     qconv.set_weight_bias(qweight, mod.bias)
    #     qconv.scale = float(act_scale)
    #     qconv.zero_point = int(act_zp)
    #
    #     return qconv

##################################################################################################

################################

class Simplenet(nn.Module):
    def __init__(self):
        super(Simplenet, self).__init__()

        cus_in = 3
        cus_out = 6
        cus_kernel = 5
        self.count = 1

        #self.check = nn.ModuleList([nn.Conv2d(cus_in, cus_out, kern) for kern in cus_kernel])   ###  Using Custom Conv2d
        #print("test--", self.check)

        #for mod in self.modules():
            #print("test--", mod)

        self.conv1 = Conv2d(3, 6, 5)
        self.relu_conv1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.relu_conv2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)    ###  Using Custom Linear
        self.relu_fc1 = nn.ReLU()
        self.fc2 = nn.Linear(120, 84)
        self.relu_fc2 = nn.ReLU()
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):

        #test = nn.ModuleList()
        #print("test-----------", test)
        #if (self.count == 1):
        #    for mod in self.modules():
        #        print("test--", mod)

        #self.count = self.count + 1
        x = self.pool1(self.relu_conv1(self.conv1(x)))
        x = self.pool2(self.relu_conv2(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = self.relu_fc1(self.fc1(x))
        x = self.relu_fc2(self.fc2(x))
        x = self.fc3(x)
        x = F.log_softmax(x, dim=1)
        return x

#########################################################################################################
##################################   Loading Model and Quantization ###############################

model = Simplenet()
model = torch.nn.DataParallel(model)
# device = 'cpu'
# model.cpu()

quantizer = quantization.PostTrainLinearQuantizer(model, model_activation_stats='/home/soumyadeep/distiller/examples/classifier_compression/logs/2019.10.10-234320/configs/acts_quantization_stats.yaml')
dummy_input = Variable(torch.randn(4, 3, 32, 32), requires_grad=True)
quantizer.prepare_model(dummy_input)
#quantizer.prepare_model()

# model.to(device)
checkpoint = torch.load('/home/soumyadeep/distiller/examples/classifier_compression/logs/2019.10.10-234320/quantized_checkpoint.pth.tar')
model.load_state_dict(checkpoint['state_dict'], strict=True)
model = model.to(torch.device('cuda'))
print('<<<<<<<<<<<<<<<<< Model Loaded !!!! >>>>>>>>>>>>>>>>>>')

#################################################################################################
######################################   Prediction Part ########################################

def test_label_predictions(model, device, test_loader):
    model.eval()
    actuals = []
    predictions = []
    correct = 0

    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            prediction = output.argmax(dim=1, keepdim=True)
            actuals.extend(target.view_as(prediction))
            predictions.extend(prediction)
            correct += prediction.eq(target.view_as(prediction)).sum().item()

    return [i.item() for i in actuals], [i.item() for i in predictions], correct


#########################################################################################
##########################################  Accuracy ####################################

device_name = 'cuda'
actuals, predictions, correct = test_label_predictions(model, device_name, testloader)
# print("actuals ---",actuals)
# print("prediction ---", predictions)
total_num_data = len(testloader.dataset)
accuracy = (float(correct / total_num_data)) * 100
print("--acuracy---", accuracy)

##################################################################################################
#########################################  CODE END ##############################################