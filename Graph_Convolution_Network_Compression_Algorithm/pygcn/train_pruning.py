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
import csv

from pygcn.utils import load_data, accuracy, to_var, prune_rate
from pygcn.models import Masked_GCN, GCN
from pygcn.enhanced_compression_algorithm import decode_compression_module, compression_module
from pygcn.pruning_methods import weight_prune
from pygcn.huffman_encoding_module import huffman_encode_model, huffman_decode_model
from pygcn.weight_sharing_dict_normal import apply_weight_sharing

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
    loss_train_data.append(1/loss_train)
    acc_diff_data.append(acc_train)

    #set hyper parameters
    alpha = 0.01
    iters = 1
    theta = 1e-5
    theta = np.zeros(len(loss_train_data))

    #globals()
    g, cost = gradientDescent(loss_train_data, acc_diff_data, theta, iters, alpha)

    finalCost = computeCost(loss_train_data, acc_diff_data, g)
    #print("final_cost----", finalCost)
    sense_check = 1 - finalCost

    decimal_pos = 2
    tune_factor_1 = -0.12
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

    if decimal_pos == 2:
        decimal_pos = 4
    elif decimal_pos == 4:
        decimal_pos = 2
    else:
        decimal_pos = 3
    sense_dict = {2: 'Low', 3: 'Medium', 4: 'High'}
    return decimal_pos, sense_dict[decimal_pos], sense_check

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

    args = parser.parse_args()
    args.cuda = not args.no_cuda and torch.cuda.is_available()

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed(args.seed)

    # Load data
    adj, features, labels, idx_train, idx_val, idx_test = load_data()

    # Model and optimizer
    model = Masked_GCN(nfeat=features.shape[1],
                       nhid=args.hidden,
                       nclass=labels.max().item() + 1,
                       dropout=args.dropout)
    optimizer = optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)

    # model = torch.nn.DataParallel(model)
    if args.cuda:
        model.cuda()
        features = features.cuda()
        adj = adj.cuda()
        labels = labels.cuda()
        idx_train = idx_train.cuda()
        idx_val = idx_val.cuda()
        idx_test = idx_test.cuda()

    ############### Solve the argument bug ###################

    return args, model, optimizer, adj, features, labels, idx_train, idx_val, idx_test


################################ Training Code ##################################################

def train(epoch, model, optimizer, adj, features, labels, idx_train, idx_val):
    t = time.time()
    model.train()
    optimizer.zero_grad()
    output = model(features, adj)
    loss_train = F.nll_loss(output[idx_train], labels[idx_train])
    acc_train = accuracy(output[idx_train], labels[idx_train])

    decimal_pos, sense_val, sense_check = cost_function_compute(loss_train, acc_train)

    loss_train.backward()
    optimizer.step()

    model = approximate_model(model, decimal_pos)

    if not args.fastmode:
        model.eval()
        output = model(features, adj)

    loss_val = F.nll_loss(output[idx_val], labels[idx_val])
    acc_val = accuracy(output[idx_val], labels[idx_val])
    print('Epoch: {:04d}'.format(epoch + 1),
          'loss_train: {:.4f}'.format(loss_train.item()),
          'acc_train: {:.4f}'.format(acc_train.item()),
          'loss_val: {:.4f}'.format(loss_val.item()),
          'acc_val: {:.4f}'.format(acc_val.item()),
          'time: {:.4f}s'.format(time.time() - t))

    # sense_check = 0.1
    # sense_val = 'High'
    # decimal_pos = 2

    return model, loss_val, optimizer, sense_val, sense_check, decimal_pos


##################################### Model Testing Code ###################

def test(model, adj, features, labels, idx_train, idx_test):
    model.eval()
    output = model(features, adj)
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


########################## Main Function ####################

if __name__ == '__main__':

    path_save_model = "./model_trained/model_checkpoint_new_1.pt"
    weight_model_path = "./model_trained/weight_model_checkpoint_compressed.pt"

    ######### Training settings ##########

    args, model, optimizer, adj, features, labels, idx_train, idx_val, idx_test = gcn_train_settings()

    ### prune the weights
    # masks = weight_prune(model, args.pruning_perc)
    # model.set_masks(masks)

    ############## edited the training code for argument parsing ##################

    t_total = time.time()
    store_sensitivity = []
    store_scaling_factor = []

    for epoch in range(args.epochs):
        model, loss_val, optimizer, sense, sense_check, decimal_pos = train(epoch, model, optimizer, adj, features, labels, idx_train, idx_val)
        #store_scaling_factor.append(decimal_pos)
        #store_sensitivity.append(float(sense_check))

    #np.savetxt('sensitivity_data.csv', store_sensitivity, delimiter=",", fmt='%s')
    #np.savetxt('scaling_factor.csv', store_scaling_factor, delimiter=",", fmt='%s')

    # with open('sensitivity_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    #     writer.writerows(store_sensitivity)
    #     # for i in range(0, len(store_sensitivity), 1):
    #     #     writer.writerows(store_sensitivity[i])
    #
    # with open('scaling_factore_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(store_scaling_factor)
        # for i in range(0, len(store_scaling_factor), 1):
        #     writer.writerows(store_scaling_factor[i])
    ##############################################################################

    print("Training and Optimization Finished!")
    print("Total time elapsed: {:.4f}s".format(time.time() - t_total))

    ######### Testing ################

    test(model, adj, features, labels, idx_train, idx_test)

    ########### compression #########

    #final_data_type = torch.float
    #sense = 'Low'
    model, dictionary_compressed_data, final_data_type = compression_module(model, compression_type=0, sensitivity=sense)

    ##### Saving the model #########

    compression_mode_val = 0

    checkpoint_new = {
        'state_dict': model.state_dict(),
        'optimizer': optimizer.state_dict(),
        'features': features,
        'labels': labels,
        'compression_dataType': final_data_type,
    }

    checkpoint_new_weight = {
        'state_dict': model.state_dict(),
        'dictTable': dictionary_compressed_data,
        'dataType': final_data_type,
        'mode': 0,
    }

    checkpoint_only_weight = {
        'state_dict': model.state_dict(),
    }

    path_1 = "./model_trained/uncompressed_weight_model.pt"
    path_2 = "./model_trained/compressed_weight_model.pt"

    #stat1 = save_model_checkpoint(checkpoint_only_weight, path_1)
    stat2 = save_model_checkpoint(checkpoint_new_weight, path_2)

    status_new = False

    status_new = save_model_checkpoint(checkpoint_new, weight_model_path)
    if status_new:
        print("--- The Weight Model is saved as checkpoint successfully in model_trained ----")
    else:
        print("--- The weight model not saved -----")

    print("---pruned and compressed weights generated")

    ################## Testing decode compression ############

    json_path = "./model_trained/weight_model_dict_feather.json"
    path= "./model_trained/weight_model_dict_feather.pt"
    Model_inference, optimizer, features, labels, final_data_type = decode_compression_module(model, optimizer, weight_model_path, path, compression_mode=0)

    ######### Re testing Compression Accuracy Verification ################

    test(Model_inference, adj, features, labels, idx_train, idx_test)

    ########### compression #########
