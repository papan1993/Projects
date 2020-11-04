from __future__ import division
from __future__ import print_function

import time
import argparse
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
import shutil
import math

# from pygcn.extra_code.train_copy_file import args
from pygcn.utils_for_inference import load_data, accuracy, to_var, prune_rate
from pygcn.models import Masked_GCN, GCN
from pygcn.enhanced_compression_algorithm import compression_module
from pygcn.pruning_methods import weight_prune, filter_prune
from pygcn.huffman_encoding_module import huffman_encode_model, huffman_decode_model
from pygcn.weight_sharing_dict_normal import apply_weight_sharing


################   Approximate Function ###########

loss_train_data = []
acc_diff_data = []

################   Approximate Function ###########

def computeCost(X,y,theta):
    tobesummed = np.power(((X @ theta.T)-y),2)
    return np.sum(tobesummed)/(2 * len(X))

def gradientDescent(X,y,theta,iters,alpha):
    cost = np.zeros(iters)
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
        cost[i] = computeCost(X, y, theta)

    return theta,cost

def cost_function_compute(loss_train, acc_train):

    loss_train = loss_train.detach().numpy()
    acc_train = acc_train.numpy()

    globals()
    loss_train_data.append(loss_train)
    acc_diff_data.append(acc_train)

    #set hyper parameters
    alpha = 0.01
    iters = 1
    theta = 1e-5
    theta = np.zeros(len(loss_train_data))

    #globals()
    g, cost = gradientDescent(loss_train_data, acc_diff_data, theta, iters, alpha)

    finalCost = computeCost(loss_train_data, acc_diff_data, g)
    print("final_cost----", finalCost)
    sense_check = 1 - finalCost

    decimal_pos = 2
    tune_factor_1 = 0.65
    tune_factor_2 = 2
    val = (1 - tune_factor_1) - sense_check
    if val < 0:
        val = 0
    max_v = 1
    min_v = 0
    b = 8
    a = 1
    new_val = (((b-a)*(val - min_v))/(max_v - min_v))+a
    new_val = math.ceil(new_val)
    if new_val < tune_factor_2:
        decimal_pos = 2
    else:
        decimal_pos = new_val

    sense_dict = {2: 'Low', 3: 'Medium', 4: 'High'}
    return decimal_pos, sense_dict[decimal_pos]

#################  Deep Pruning Concept ######################

def prune_filter_min_function(value_layer):
    unique_vals, count_frequency,  = np.unique(value_layer, return_counts=True)


def approximate_model(model, decimal_pos):

    #########  Approximate both weight and bias

    for name, param in model.named_parameters():
        layer_val = param.data.numpy()
        layer_approx = np.round(layer_val, decimals=decimal_pos)
        #prune_filter_min_function(layer_approx)
        layer_approx = torch.from_numpy(layer_approx)
        #layer_approx = torch.as_tensor(layer_approx, dtype=torch.float16)
        param.data = layer_approx

    # layer_1 = model.gc1.weight.data
    # layer_1 = layer_1.numpy()
    # layer_1_approx = np.round(layer_1, decimals=decimal_pos)
    # prune_filter_min_function(layer_1_approx)
    # layer_1_approx = torch.from_numpy(layer_1_approx)
    # layer_1_approx = to_var(layer_1_approx, requires_grad=False)
    # model.gc1.weight.data = layer_1_approx
    #
    # layer_2 = model.gc2.weight.data
    # layer_2 = layer_2.numpy()
    # layer_2_approx = np.round(layer_2, decimals=decimal_pos)
    # layer_2_approx = torch.from_numpy(layer_2_approx)
    # layer_2_approx = to_var(layer_2_approx, requires_grad=False)
    # model.gc2.weight.data = layer_2_approx

    return model


############################### Function for training settings ###################

def gcn_train_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='Disables CUDA training.')
    parser.add_argument('--fastmode', action='store_true', default=False,
                        help='Validate during training pass.')
    parser.add_argument('--seed', type=int, default=42, help='Random seed.')
    parser.add_argument('--epochs', type=int, default=200,
                        help='Number of epochs to train.')
    parser.add_argument('--lr', type=float, default=0.01,
                        help='Initial learning rate.')
    parser.add_argument('--weight_decay', type=float, default=5e-4,
                        help='Weight decay (L2 loss on parameters).')
    parser.add_argument('--hidden', type=int, default=16,
                        help='Number of hidden units.')
    parser.add_argument('--dropout', type=float, default=0.5,
                        help='Dropout rate (1 - keep probability).')
    parser.add_argument('--pruning_perc', type=float, default=90.,
                        help='Pruning Percentage')

    args_new = parser.parse_args()
    args_new.cuda = not args_new.no_cuda and torch.cuda.is_available()
    device = torch.device("cuda" if args_new.cuda else 'cpu')

    np.random.seed(args_new.seed)
    torch.manual_seed(args_new.seed)
    if args_new.cuda:
        torch.cuda.manual_seed(args_new.seed)

    # Load data
    adj_new, features_new, labels_new, idx_train_new, idx_val_new, idx_test_new = load_data()

    # print("i received data")

    # print("before_model_initilaization")

    # Model and optimizer
    Model_inference = Masked_GCN(nfeat=features_new.shape[1],
                                 nhid=args_new.hidden,
                                 nclass=labels_new.max().item() + 1,
                                 dropout=args_new.dropout)

    # print("before_this optimizer")

    optimizer_new = optim.Adam(Model_inference.parameters(), lr=args_new.lr, weight_decay=args_new.weight_decay)

    # model = torch.nn.DataParallel(model)
    if args_new.cuda:
        Model_inference.cuda()
        features = features_new.cuda()
        adj = adj_new.cuda()
        labels = labels_new.cuda()
        idx_train = idx_train_new.cuda()
        idx_val = idx_val_new.cuda()
        idx_test = idx_test_new.cuda()

    ############### Solve the argument bug ###################

    return args_new, Model_inference, optimizer_new, adj_new, features_new, labels_new, idx_train_new, idx_val_new, idx_test_new, device


################################ Training Code ##################################################

def train(epoch, Model_inference, optimizer, adj, features, labels, idx_train, idx_val, device):
    t = time.time()
    Model_inference.train()
    optimizer.zero_grad()
    output = Model_inference(features, adj)
    loss_train = F.nll_loss(output[idx_train], labels[idx_train])
    acc_train = accuracy(output[idx_train], labels[idx_train])

    decimal_pos, sense_val = cost_function_compute(loss_train, acc_train)

    loss_train.backward()

    # zero-out all the gradients corresponding to the pruned connections

    for name, p in Model_inference.named_parameters():
        if 'mask' in name:
            continue
        tensor = p.data.cpu().numpy()
        grad_tensor = p.grad.data.cpu().numpy()
        grad_tensor = np.where(tensor==0, 0, grad_tensor)
        p.grad.data = torch.from_numpy(grad_tensor).to(device)

    optimizer.step()

    Model_inference = approximate_model(Model_inference, decimal_pos)

    if not args.fastmode:
        Model_inference.eval()
        output = Model_inference(features, adj)

    loss_val = F.nll_loss(output[idx_val], labels[idx_val])
    acc_val = accuracy(output[idx_val], labels[idx_val])
    print('Epoch: {:04d}'.format(epoch + 1),
          'loss_train: {:.4f}'.format(loss_train.item()),
          'acc_train: {:.4f}'.format(acc_train.item()),
          'loss_val: {:.4f}'.format(loss_val.item()),
          'acc_val: {:.4f}'.format(acc_val.item()),
          'time: {:.4f}s'.format(time.time() - t))

    return Model_inference, loss_val, optimizer, sense_val


##################################### Model Testing Code ###################

def test(Model_inference, adj, features, labels, idx_train, idx_test):
    Model_inference.eval()
    output = Model_inference(features, adj)
    loss_test = F.nll_loss(output[idx_test], labels[idx_test])
    acc_test = accuracy(output[idx_test], labels[idx_test])
    print("Test set results:",
          "loss= {:.4f}".format(loss_test.item()),
          "accuracy= {:.4f}".format(acc_test.item()))


#################### Saving Checkpoint Model function ###############

def save_model_checkpoint(state, path_save_model):
    status = False
    f_path = path_save_model
    torch.save(state, f_path)  # save checkpoint data to the path given, checkpoint_path
    status = True
    return status


##################  Load Model Checkpoint ########################

def load_ckp(checkpoint_fpath, Model_inference, optimizer):
    checkpoint = torch.load(checkpoint_fpath)  # load check point
    Model_inference.load_state_dict(checkpoint['state_dict'])  # initialize state_dict from checkpoint to model
    Model_inference.eval()
    optimizer.load_state_dict(checkpoint['optimizer'])  # initialize optimizer from checkpoint to optimizer
    # adj = checkpoint['adj']
    final_data_type = checkpoint['compression_dataType']
    features = checkpoint['features']
    labels = checkpoint['labels']

    return Model_inference, optimizer, features, labels, final_data_type


########################## Main Fucntion ####################

if __name__ == '__main__':

    path_save_model = "./model_trained/weight_model_checkpoint_uncompressed.pt"
    pruned_weight_model_path = "./model_trained/pruned_weight_model_checkpoint.pt"

    ######### Training settings ##########

    args, Model_inference, optimizer, adj, features, labels, idx_train, idx_val, idx_test, device = gcn_train_settings()

    ############################### Load Model ######################

    print("before loading")

    Model_inference, optimizer, features, labels, final_data_type = load_ckp(path_save_model, Model_inference,
                                                                             optimizer)

    ##################################### Pruning Train and Inference ##########################################

    ### prune the weights
    masks_1 = weight_prune(Model_inference, args.pruning_perc)
    Model_inference.set_masks(masks_1)

    ### prune the filter
    masks_2 = filter_prune(Model_inference, args.pruning_perc)
    Model_inference.set_masks(masks_2)

    ######## Re-train model #####################

    t_total = time.time()

    for epoch in range(args.epochs):
        Model_inference, loss_val, optimizer, sense = train(epoch, Model_inference, optimizer, adj, features, labels, idx_train, idx_val, device)

    ##############################################################################

    print("Training and Optimization Finished!")
    print("Total time elapsed: {:.4f}s".format(time.time() - t_total))

    ######### Testing ################

    test(Model_inference, adj, features, labels, idx_train, idx_test)

    ##########  Compression  ##########

    Model_inference, dictionary_compressed_data, final_data_type = compression_module(Model_inference, compression_type = 0, sensitivity = sense)

    #######################  Saving the weights ######################

    checkpoint_new = {
        'state_dict': Model_inference.state_dict(),
        'optimizer': optimizer.state_dict(),
        'features': features,
        'labels': labels,
        'compression_dataType': final_data_type,
    }

    status_new = save_model_checkpoint(checkpoint_new, pruned_weight_model_path)
    if status_new:
        print("--- The pruned anf compressed Weight Model is saved as checkpoint successfully in model_trained ----")
    else:
        print("--- The pruned weight model not saved -----")

##################################################
