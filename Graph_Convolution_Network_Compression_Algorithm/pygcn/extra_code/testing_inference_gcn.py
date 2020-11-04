from __future__ import division
from __future__ import print_function

import time
import argparse
import numpy as np

import torch
import torch.nn.functional as F
import torch.optim as optim

from pygcn.utils import load_data, accuracy
from pygcn.models import GCN

###################

import shutil

################

############################### Function for training settings ###################

def gcn_model_settings():

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

	args = parser.parse_args()
	args.cuda = not args.no_cuda and torch.cuda.is_available()

	np.random.seed(args.seed)
	torch.manual_seed(args.seed)
	if args.cuda:
		torch.cuda.manual_seed(args.seed)

	# Load data
	adj, features, labels, idx_train, idx_val, idx_test = load_data()

	# Model and optimizer
	model = GCN(nfeat=features.shape[1],
		        nhid=args.hidden,
		        nclass=labels.max().item() + 1,
		        dropout=args.dropout)
	optimizer = optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)

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

##################################################################################

##################################### Model Testing Code after loading for inference ################### 

def test_loading(model, adj, features, labels, idx_train, idx_test):
    model.eval()
    output = model(features, adj)
    loss_test = F.nll_loss(output[idx_test], labels[idx_test])
    acc_test = accuracy(output[idx_test], labels[idx_test])
    print("Test set results- after loading model from checkpoint : ",
          "loss= {:.4f}".format(loss_test.item()),
          "accuracy= {:.4f}".format(acc_test.item()))

############################################################################

##################  Load Model Checkpoint ########################

def load_ckp(checkpoint_fpath, args, model, optimizer, adj, features, labels, idx_train, idx_val, idx_test):

    checkpoint = torch.load(checkpoint_fpath)  # load check point
    
    model.load_state_dict(checkpoint['state_dict']) # initialize state_dict from checkpoint to model
    #model.eval()
    
    optimizer.load_state_dict(checkpoint['optimizer']) # initialize optimizer from checkpoint to optimizer
    
    valid_loss_min = checkpoint['valid_loss_min'] # initialize valid_loss_min from checkpoint to valid_loss_min

    #args = checkpoint['args']
    #adj = checkpoint['adj']
    #features = checkpoint['features']
    labels = checkpoint['labels']
    #idx_train = checkpoint['train_data']
    #idx_val = checkpoint['val_data']
    #idx_test = checkpoint['test_data']
  
    return model, optimizer, checkpoint['epoch'], valid_loss_min, args, adj, features, labels, idx_train, idx_val, idx_test # return model, optimizer, epoch value, min validation loss

###################################################################


########################## Main Fucntion ####################

if __name__ == '__main__':

	path_save_model = "./model_trained/model_checkpoint.pt"

	######### Dataset and Model loading settings ##########

	args, model, optimizer, adj, features, labels, idx_train, idx_val, idx_test = gcn_model_settings()

	##############################################################################

	##### Load the model from checkpoint ######### 

	model, optimizer, number_epochs, valid_loss_min, args, adj, features, labels, idx_train, idx_val, idx_test = load_ckp(path_save_model, args, model, optimizer, adj, features, labels, idx_train, idx_val, idx_test) 

	print("____model__loaded_____")

	print("model = ", model)
	print("optimizer = ", optimizer)
	print("number_epochs = ", number_epochs)
	print("valid_loss_min = ", valid_loss_min)
	print("valid_loss_min = {:.6f}".format(valid_loss_min))	

	################## Testing the Loaded the model for further inference ###############

	print("_____ Testing the loaded model for inference_____")

	test_loading(model, adj, features, labels, idx_train, idx_test)

	print("----------------------")

	print(model.state_dict())

##################################################
