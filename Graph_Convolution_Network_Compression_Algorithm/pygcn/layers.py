import math
import torch
from torch.nn.parameter import Parameter
from torch.nn.modules.module import Module
from pygcn.utils import to_var

##################################################################

class GraphConvolution(Module):

    def __init__(self, in_features, out_features, bias=True):
        super(GraphConvolution, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = Parameter(torch.FloatTensor(in_features, out_features))
        if bias:
            self.bias = Parameter(torch.FloatTensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.weight.size(1))
        self.weight.data.uniform_(-stdv, stdv)
        if self.bias is not None:
            self.bias.data.uniform_(-stdv, stdv)

    def forward(self, input, adj):
        support = torch.mm(input, self.weight)
        output = torch.spmm(adj, support)
        if self.bias is not None:
            return output + self.bias
        else:
            return output

    def __repr__(self):
        return self.__class__.__name__ + ' (' \
               + str(self.in_features) + ' -> ' \
               + str(self.out_features) + ')'

####################################################################

class Masked_GraphConvolution(Module):

    """
    Masked GCN layer
    """

    def __init__(self, in_features, out_features, bias=True):
        super(Masked_GraphConvolution, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = Parameter(torch.FloatTensor(in_features, out_features))
        if bias:
            self.bias = Parameter(torch.FloatTensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()
        self.mask_flag = False

    def set_mask(self, mask):
        self.mask = to_var(mask, requires_grad=False)
        #device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        #torch.device("cuda:0")
        #self.weight.data = torch.mm(self.weight.data, self.mask.data)
        self.weight.data = self.weight.data*self.mask.data
        self.mask_flag = True

    def get_mask(self):
        print(self.mask_flag)
        return self.mask

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.weight.size(1))
        self.weight.data.uniform_(-stdv, stdv)
        if self.bias is not None:
            self.bias.data.uniform_(-stdv, stdv)

    def forward(self, input, adj):
        if self.mask_flag:
            weight = self.weight*self.mask
            support = torch.mm(input, weight)

        else:
            support = torch.mm(input, self.weight)

        output = torch.spmm(adj, support)
        if self.bias is not None:
            ret = output + self.bias

            return ret
        else:
            return output

    def __repr__(self):
        return self.__class__.__name__ + ' (' \
               + str(self.in_features) + ' -> ' \
               + str(self.out_features) + ')'

########################################################################
