import numpy as np

def mergeSort(alist, array_weight):

    print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        array_lefthalf = array_weight[:mid]
        righthalf = alist[mid:]
        array_righhalf = array_weight[mid:]

        #recursion
        mergeSort(lefthalf, array_lefthalf)
        mergeSort(righthalf, array_righhalf)

        i=0
        j=0
        k=0

        while (i < len(lefthalf) and j < len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                array_weight[k] = array_lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                array_weight[k] = array_righhalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            array_weight[k] = array_lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            array_weight[k] = array_righhalf[j]
            j=j+1
            k=k+1

    print("Merging ", alist)
    print("array_merging", array_weight)

if __name__ == '__main__':
    array_weight = [4.0, 4.5, 5.0, 2.0, 2.5, 1.5, 9.5, 7.5, 5.5, 6.0, 6.5, 8.0, 8.5]
    print(len(array_weight))
    array_weight_new = np.asarray(array_weight, dtype=np.float32)
    array = [10, 12, 1, 3, 6, 8, 9, 11, 7, 4, 5, 20, 15]
    print(len(array))
    array_new = np.asarray(array, dtype=np.float32)
    mergeSort(array_new, array_weight_new)
    reverse_array = np.flipud(array_new)
    reverse_array_weight = np.flipud(array_weight_new)
    print(reverse_array)
    print(reverse_array_weight)

    name = str('papan_pap')
    globals()[name] = {}
    print("check")

    # sort_count_frequency = sorted(count_frequency, reverse=True)
    # unique_weights_copy = unique_weights
    # count_frequency_copy = count_frequency
    # count_frequency = np.asarray(count_frequency)
    # mergeSort_advance(count_frequency, unique_weights)
    # unique_weights_sorted = np.flipud(unique_weights)
    # count_frequency_sorted = np.flipud(count_frequency)

    # globals()[layer_dict_name_1] = {}
    #globals()[layer_dict_name_1] = np.empty(layer_data.shape)

    #globals()[layer_dict_name_2] = {}

    #compressed_model_data = {layer_dict_name_1 : layer_buf_table, layer_dict_name_2 : layer_dictionary_data}

def mergeSort_advance(alist, array_weight):

    print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        array_lefthalf = array_weight[:mid]
        righthalf = alist[mid:]
        array_righhalf = array_weight[mid:]

        #recursion
        mergeSort_advance(lefthalf, array_lefthalf)
        mergeSort_advance(righthalf, array_righhalf)

        i=0
        j=0
        k=0

        while (i < len(lefthalf) and j < len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                array_weight[k] = array_lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                array_weight[k] = array_righhalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            array_weight[k] = array_lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            array_weight[k] = array_righhalf[j]
            j=j+1
            k=k+1

    print("Merging ", alist)
    print("array_merging", array_weight)


import json
import zlib
import feather

### retrain and test the model
#
# ######## Re-train model #####################
#
# t_total = time.time()
#
# ############## edited the training code for argument parsing ##################
#
# for epoch in range(args.epochs):
# 	model, loss_val, optimizer = train(epoch, model, optimizer, adj, features, labels, idx_train, idx_val)
#
# ##############################################################################
#
# print("Training and Optimization Finished!")
# print("Total time elapsed: {:.4f}s".format(time.time() - t_total))
#
# ######### Testing ################
#
# test(model, adj, features, labels, idx_train, idx_test)

###############################################################################

################## Load the model for further inference ###############

###test_loading(model, adj, features, labels, idx_train, idx_test)

##################################################

# Model and optimizer
# model_new = Masked_GCN(nfeat=features.shape[1],
# 	        nhid=args.hidden,
# 	        nclass=labels.max().item() + 1,
# 	        dropout=args.dropout)
# optimizer_new = optim.Adam(model_new.parameters(), lr=args.lr, weight_decay=args.weight_decay)
#
# model = torch.nn.DataParallel(model)
#
# if args.cuda:
# 	model_new.cuda()
# 	features = features.cuda()
# 	adj = adj.cuda()
# 	labels = labels.cuda()
# 	idx_train = idx_train.cuda()
# 	idx_val = idx_val.cuda()
# 	idx_test = idx_test.cuda()