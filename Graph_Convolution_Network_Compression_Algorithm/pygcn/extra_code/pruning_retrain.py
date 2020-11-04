from __future__ import division
from __future__ import print_function

import time
import argparse
import numpy as np

import torch
import torch.nn.functional as F
import torch.optim as optim

###################

import shutil

from pygcn.extra_code.train_copy_file import args
from pygcn.utils import load_data, accuracy
from utils import to_var, prune_rate
from pygcn.models import GCN
from models import Masked_GCN
from pruning_methods import weight_prune


################

# Training settings

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

    #model = torch.nn.DataParallel(model)
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
    loss_train.backward()
    optimizer.step()

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

    return model, loss_val, optimizer


#######################  ###############################

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

    #    if is_best:    				# if it is a best model, min validation loss
    #        best_fpath = best_model_path
    #        shutil.copyfile(f_path, best_fpath)    # copy that checkpoint file to best path given, best_model_path

    return status






########################## Main Fucntion ####################


