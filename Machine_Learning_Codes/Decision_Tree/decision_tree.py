# decision_tree.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# personal and educational purposes provided that (1) you do not distribute
# or publish solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UT Dallas, including a link to http://cs.utdallas.edu.
#
# This file is part of Homework for CS6375: Machine Learning.
# Gautam Kunapuli (gautam.kunapuli@utdallas.edu)
# Sriraam Natarajan (sriraam.natarajan@utdallas.edu),
# Anjum Chida (anjum.chida@utdallas.edu)
#
#
# INSTRUCTIONS:
# ------------
# 1. This file contains a skeleton for implementing the ID3 algorithm for
# Decision Trees. Insert your code into the various functions that have the
# comment "INSERT YOUR CODE HERE".
#
# 2. Do NOT modify the classes or functions that have the comment "DO NOT
# MODIFY THIS FUNCTION".
#
# 3. Do not modify the function headers for ANY of the functions.
#
# 4. You may add any other helper functions you feel you may need to print,
# visualize, test, or save the data and results. However, you MAY NOT utilize
# the package scikit-learn OR ANY OTHER machine learning package in THIS file.

import numpy as np
import os
import graphviz

###############################  MY INSERTED CODE  ##############################

import math
import pandas as pd
import matplotlib.pyplot as plt
import pydotplus
from collections import defaultdict, Counter
from IPython.display import Image
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from statistics import mean

################################################################################

def partition(x):
    """
    Partition the column vector x into subsets indexed by its unique values (v1, ... vk)

    Returns a dictionary of the form
    { v1: indices of x == v1,
      v2: indices of x == v2,
      ...
      vk: indices of x == vk }, where [v1, ... vk] are all the unique values in the vector z.
    """

    # INSERT YOUR CODE HERE
    # raise Exception('Function not yet implemented!')

    ###############################  MY INSERTED CODE  ##############################

    part_dict = {}

    for i in range(0, len(x), 1):
        temp_1 = x[i]

        if (temp_1 in part_dict):
            part_dict[x[i]].append(i)
        else:
            part_dict[x[i]] = []
            part_dict[x[i]].append(i)

    return part_dict


################################################################################


def entropy(y):
    """
    Compute the entropy of a vector y by considering the counts of the unique values (v1, ... vk), in z

    Returns the entropy of z: H(z) = p(z=v1) log2(p(z=v1)) + ... + p(z=vk) log2(p(z=vk))
    """

    # INSERT YOUR CODE HERE
    # raise Exception('Function not yet implemented!')

    ###############################  MY INSERTED CODE  ##############################

    entropy_val = 0           ### Initialise 0 as no change
    final_entropy = 0
    y_new = np.array(y)

    for j in set(y_new):
        temp_2 = (y_new == j).sum()
        temp_2 = temp_2 / len(y_new)
        entropy_val = entropy_val + (temp_2 * math.log2(temp_2))

    final_entropy = -entropy_val ### Sign for entropy
    return final_entropy

##############################################################################


def mutual_information(x, y):
    """
    Compute the mutual information between a data column (x) and the labels (y). The data column is a single attribute
    over all the examples (n x 1). Mutual information is the difference between the entropy BEFORE the split set, and
    the weighted-average entropy of EACH possible split.

    Returns the mutual information: I(x, y) = H(y) - H(y | x)
    """

    # INSERT YOUR CODE HERE
    # raise Exception('Function not yet implemented!')

    ###############################  MY INSERTED CODE  ##############################

    sum_h_x_y = 0
    dict_sum = 0
    mutual_info = 0

    ### load entropy value and data
    entropy_y = entropy(y)
    df_load = pd.DataFrame(x)
    mydict = defaultdict(list)
    tot_x = df_load.size

    for ind, rw in df_load[0].iteritems():
        mydict[rw].append(ind)

    for val in mydict.values():
        dict_sum = dict_sum + (len(val))

    for key, values in mydict.items():

        temp1 = y[values].size
        temp2 = (temp1 / tot_x)
        temp3 = entropy(y[x == key])
        ent_y_x = (temp2 * temp3)
        sum_h_x_y = sum_h_x_y + ent_y_x

    mutual_info = (entropy_y - sum_h_x_y)
    return mutual_info

###############################################################################


def id3(x, y, attribute_value_pairs=None, depth=0, max_depth=5):
    """
    Implements the classical ID3 algorithm given training data (x), training labels (y) and an array of
    attribute-value pairs to consider. This is a recursive algorithm that depends on three termination conditions
        1. If the entire set of labels (y) is pure (all y = only 0 or only 1), then return that label
        2. If the set of attribute-value pairs is empty (there is nothing to split on), then return the most common
           value of y (majority label)
        3. If the max_depth is reached (pre-pruning bias), then return the most common value of y (majority label)
    Otherwise the algorithm selects the next best attribute-value pair using INFORMATION GAIN as the splitting criterion
    and partitions the data set based on the values of that attribute before the next recursive call to ID3.

    The tree we learn is a BINARY tree, which means that every node has only two branches. The splitting criterion has
    to be chosen from among all possible attribute-value pairs. That is, for a problem with two features/attributes x1
    (taking values a, b, c) and x2 (taking values d, e), the initial attribute value pair list is a list of all pairs of
    attributes with their corresponding values:
    [(x1, a),
     (x1, b),
     (x1, c),
     (x2, d),
     (x2, e)]
     If we select (x2, d) as the best attribute-value pair, then the new decision node becomes: [ (x2 == d)? ] and
     the attribute-value pair (x2, d) is removed from the list of attribute_value_pairs.

    The tree is stored as a nested dictionary, where each entry is of the form
                    (attribute_index, attribute_value, True/False): subtree
    * The (attribute_index, attribute_value) determines the splitting criterion of the current node. For example, (4, 2)
    indicates that we test if (x4 == 2) at the current node.
    * The subtree itself can be nested dictionary, or a single label (leaf node).
    * Leaf nodes are (majority) class labels

    Returns a decision tree represented as a nested dictionary, for example
    {(4, 1, False):
        {(0, 1, False):
            {(1, 1, False): 1,
             (1, 1, True): 0},
         (0, 1, True):
            {(1, 1, False): 0,
             (1, 1, True): 1}},
     (4, 1, True): 1}
    """

    # INSERT YOUR CODE HERE. NOTE: THIS IS A RECURSIVE FUNCTION.
    # raise Exception('Function not yet implemented!')

    ###############################  MY INSERTED CODE  ##############################

    df_new = pd.DataFrame(x)
    label_y = pd.DataFrame(y)
    att_val_list = list()
    mutual_info = []
    final_tree = {}

    if (label_y[0].unique().size == 1):
        label = label_y[0].unique()
        return label[0]

    if (attribute_value_pairs == None):
        att_val_list = list()

        for ind in df_new.columns:
            for val in df_new[ind].unique():
                att_val_list.append((ind, val))
        attribute_value_pairs = att_val_list

    if (depth == max_depth or len(attribute_value_pairs) == 0):
        temp_4 = 0
        label_y_list = Counter(y)
        for key_val in label_y_list:
            if (label_y_list[key_val] > temp_4):
                temp_4 = label_y_list[key_val]
                label_y_key = key_val
        return label_y_key


    for i, j in attribute_value_pairs:
        mutual_info.append(mutual_information((x[:, i] == j), y))

    attr_d, value = attribute_value_pairs[np.argmax(mutual_info)]
    x_partitions = partition(x[:, attr_d] == value)
    attribute_value_pairs = attribute_value_pairs.remove((attr_d, value))


    for key, val in x_partitions.items():
        sub_parts_x = x.take(val, axis=0)
        sub_labels_y = y.take(val, axis=0)
        dec_val = bool(key)
        final_tree[(attr_d, value, dec_val)] = id3(sub_parts_x, sub_labels_y, attribute_value_pairs = attribute_value_pairs, depth = depth+1, max_depth = max_depth)

    return final_tree

##########################################################################################################################


def predict_example(x, tree):
    """
    Predicts the classification label for a single example x using tree by recursively descending the tree until
    a label/leaf node is reached.

    Returns the predicted label of x according to tree
    """

    # INSERT YOUR CODE HERE. NOTE: THIS IS A RECURSIVE FUNCTION.
    # raise Exception('Function not yet implemented!')

    ###############################  MY INSERTED CODE  ##############################

    try:
        len_tree = len(tree.keys())
    except Exception as e:
        return tree

    predict_list = list(tree.keys())[0]

    if x[predict_list[0]] == predict_list[1]:
        return predict_example(x, tree[(predict_list[0], predict_list[1], True)])
    else:
        return predict_example(x, tree[(predict_list[0], predict_list[1], False)])

####################################################################################


def compute_error(y_true, y_pred):
    """
    Computes the average error between the true labels (y_true) and the predicted labels (y_pred)

    Returns the error = (1/n) * sum(y_true != y_pred)
    """

    # INSERT YOUR CODE HERE
    # raise Exception('Function not yet implemented!')

    ###############################  MY INSERTED CODE  ##############################

    computed_error = 0
    count_err = 0

    for i in range(0, len(y_true), 1):
        if (y_true[i] != y_pred[i]):
            count_err = count_err + 1

    computed_error = count_err / len(y_true)
    return computed_error

####################################################################


def pretty_print(tree, depth=0):
    """
    Pretty prints the decision tree to the console. Use print(tree) to print the raw nested dictionary representation
    DO NOT MODIFY THIS FUNCTION!
    """
    if depth == 0:
        print('TREE')

    for index, split_criterion in enumerate(tree):
        sub_trees = tree[split_criterion]

        # Print the current node: split criterion
        print('|\t' * depth, end='')
        print('+-- [SPLIT: x{0} = {1} {2}]'.format(split_criterion[0], split_criterion[1], split_criterion[2]))

        # Print the children
        if type(sub_trees) is dict:
            pretty_print(sub_trees, depth + 1)
        else:
            print('|\t' * (depth + 1), end='')
            print('+-- [LABEL = {0}]'.format(sub_trees))


def render_dot_file(dot_string, save_file, image_format='png'):
    """
    Uses GraphViz to render a dot file. The dot file can be generated using
        * sklearn.tree.export_graphviz()' for decision trees produced by scikit-learn
        * to_graphviz() (function is in this file) for decision trees produced by  your code.
    DO NOT MODIFY THIS FUNCTION!
    """
    if type(dot_string).__name__ != 'str':
        raise TypeError('visualize() requires a string representation of a decision tree.\nUse tree.export_graphviz()'
                        'for decision trees produced by scikit-learn and to_graphviz() for decision trees produced by'
                        'your code.\n')

    # Set path to your GraphViz executable here
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/release/bin'
    graph = graphviz.Source(dot_string)
    graph.format = image_format
    graph.render(save_file, view=True)


def to_graphviz(tree, dot_string='', uid=-1, depth=0):
    """
    Converts a tree to DOT format for use with visualize/GraphViz
    DO NOT MODIFY THIS FUNCTION!
    """

    uid += 1  # Running index of node ids across recursion
    node_id = uid  # Node id of this node

    if depth == 0:
        dot_string += 'digraph TREE {\n'

    for split_criterion in tree:
        sub_trees = tree[split_criterion]
        attribute_index = split_criterion[0]
        attribute_value = split_criterion[1]
        split_decision = split_criterion[2]

        if not split_decision:
            # Alphabetically, False comes first
            dot_string += '    node{0} [label="x{1} = {2}?"];\n'.format(node_id, attribute_index, attribute_value)

        if type(sub_trees) is dict:
            if not split_decision:
                dot_string, right_child, uid = to_graphviz(sub_trees, dot_string=dot_string, uid=uid, depth=depth + 1)
                dot_string += '    node{0} -> node{1} [label="False"];\n'.format(node_id, right_child)
            else:

                dot_string, left_child, uid = to_graphviz(sub_trees, dot_string=dot_string, uid=uid, depth=depth + 1)
                dot_string += '    node{0} -> node{1} [label="True"];\n'.format(node_id, left_child)

        else:
            uid += 1
            dot_string += '    node{0} [label="y = {1}"];\n'.format(uid, sub_trees)
            if not split_decision:
                dot_string += '    node{0} -> node{1} [label="False"];\n'.format(node_id, uid)
            else:
                dot_string += '    node{0} -> node{1} [label="True"];\n'.format(node_id, uid)

    if depth == 0:
        dot_string += '}\n'
        return dot_string
    else:
        return dot_string, node_id, uid


if __name__ == '__main__':

    ###############################  MY INSERTED CODE  ##############################

    # Load the training data
    # M = np.genfromtxt('./monks-3.train', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    # ytrn = M[:, 0]
    # Xtrn = M[:, 1:]

    # Load the test data
    # M = np.genfromtxt('./monks-3.test', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    # ytst = M[:, 0]
    # Xtst = M[:, 1:]

    ###############################  implemented decision tree with error graph  ###########################

    path_input = input(' Enter the path of monks data folder ; for example - ./monks_data : ')
    path_variables = int(input(' Enter the number of subfolders in monks dataset ; for example - 3 : '))
    sub_path = '/monks-'
    count_pic = 1
    print(" \n ---------------------------------------------- \n ")

    for i in range(1, path_variables+1, 1):
        trainPath = path_input + sub_path + str(i) + ".train"
        testPath = path_input + sub_path + str(i) + ".test"

        # Loading the training data
        M = np.genfromtxt(trainPath, missing_values=0, skip_header=0, delimiter=',', dtype=int)
        ytrn = M[:, 0]
        Xtrn = M[:, 1:]

        # Loading the test data
        M = np.genfromtxt(testPath, missing_values=0, skip_header=0, delimiter=',', dtype=int)
        ytst = M[:, 0]
        Xtst = M[:, 1:]

        trainError = {}
        testError = {}
        depth_len = 11

        for j in range(1, depth_len, 1):
            ################## decision tree of variant depth ################ 
            decs_tree = id3(Xtrn, ytrn, max_depth=j)

            ################# Calculate training error ##############
            train_pred = [predict_example(x, decs_tree) for x in Xtrn]
            trn_err = compute_error(ytrn, train_pred)

            ############### Calculate testing error ###############
            test_pred = [predict_example(x, decs_tree) for x in Xtst]
            tst_err = compute_error(ytst, test_pred)

            trainError[j] = trn_err
            testError[j] = tst_err

        # Computing Average Training Error and Test Error #########
        sum_train = 0
        for i in range(1, len(trainError)+1, 1):
            sum_train = sum_train + trainError.get(i)
        avg_train_error = round((sum_train / len(trainError)), 4)
        print(" Average Training Error for Monks dataset : " + str(count_pic) + " ---> ", avg_train_error)

        sum_test = 0
        for i in range(1, len(testError)+1, 1):
            sum_test = sum_test + testError.get(i)
        avg_test_error = round((sum_test / len(testError)), 4)
        print(" Average Testing Error for Monks dataset : " + str(count_pic) + " ---> ", avg_test_error)

        print(" \n ---------------------------- ")
        # Below we plot the testing and training error for all the depths
        plt.figure()
        plt.plot(list(trainError.keys()), list(trainError.values()), marker='o', linewidth=3, markersize=12)
        plt.plot(list(testError.keys()), list(testError.values()), marker='s', linewidth=3, markersize=12)
        plt.xlabel('Depth of Decision Tree', fontsize=16)
        plt.ylabel('Training / Test Error', fontsize=16)
        plt.xticks(list(trainError.keys()), fontsize=12)
        plt.legend(['Training Error', 'Test Error'], fontsize=16)
        plt.xscale('log')
        plt.yscale('log')
        plt.title("Error Graph for MONKS- " + str(count_pic) + " Dataset")
        plt.savefig("Error Graph for MONKS- " + str(count_pic) + " Dataset.png", dpi=300)
        count_pic = count_pic + 1
        plt.show()

    ########################################################## id3 check code #####################################################

    trainPath = path_input + sub_path + str(1) + ".train"
    testPath = path_input + sub_path + str(1) + ".test"

    # loading the training data for part-2
    M = np.genfromtxt(trainPath, missing_values=0, skip_header=0, delimiter=',', dtype=int)
    ytrn = M[:, 0]
    Xtrn = M[:, 1:]

    # loading the testing data for part-2
    M = np.genfromtxt(testPath, missing_values=0, skip_header=0, delimiter=',', dtype=int)
    ytst = M[:, 0]
    Xtst = M[:, 1:]

    for i in range(1, 6, 2):
        decs_tree = id3(Xtrn, ytrn, max_depth=i)
        pretty_print(decs_tree)
        y_pred = [predict_example(x, decs_tree) for x in Xtst]

        ######## Plotting Trees id3 #########
        dot_string = to_graphviz(decs_tree)
        render_dot_file(dot_string, './monks1_learn_id3-' + str(i))


        ######## confusion matrix using sklearn
        print("MONKS-1 DATASET : Learning using id3 : Confusion matrix for depth -> ", i)
        print(pd.DataFrame(confusion_matrix(ytst, y_pred), columns=['Predicted Positives', 'Predicted Negatives'], index=['True Positives', 'True Negatives']))
        print(" ---------------------------------------------- ")

    ################################################################  Scikit-Learn Code ############################################
    print(" \n ---------------------------------------------- \n")
    max_depth_range = 5

    for i in range(1, max_depth_range + 1, 2):
        Data_names = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']
        decs_tree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=i)
        decs_tree.fit(Xtrn, ytrn)
        #pretty_print(decs_tree)
        plot_tree(decs_tree)
        y_pred = decs_tree.predict(Xtst)

        ####### Plotting Trees scikit-learn #########
        dot_data_str = tree.export_graphviz(decs_tree, out_file=None, feature_names=Data_names, filled=True, rounded=True, special_characters=True)
        graph_skl = pydotplus.graph_from_dot_data(dot_data_str)
        graph_skl.write_png('monks1_learn_sklearn-' + str(i) + '.png')
        #Image(filename='monks1_learn_sklearn-' + str(i) + '.png')

        ########## calculating and printing the confusion matrix using sklearn
        print("MONKS-1 DATASET : Learning using scikit-learn : Confusion matrix for depth -> ", i)
        print(pd.DataFrame(confusion_matrix(ytst, y_pred), columns=['Predicted Positives', 'Predicted Negatives'], index=['True Positives', 'True Negatives']))
        print(" ---------------------------------------------- ")

    ################################################################### UCI dataset - breast cancer #######################################################################

    print(" \n ---------------------------------------------- \n ")
    split_fraction = 0.3
    M = np.genfromtxt('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    y = M[:, 10]
    x = M[:, 0:10]

    Xtrn, Xtst, ytrn, ytst = train_test_split(x, y, test_size=split_fraction, random_state=42)
    train_mean = [Xtrn.mean(axis=0)]
    confusionmatrix_id3 = {}
    confusionmatrix_scikit = {}

    for i in range(10):
        for j in range(len(Xtrn[i])):
            if Xtrn[i][j] <= train_mean[0][i]:
                Xtrn[i][j] = 0
            else:
                Xtrn[i][j] = 1

    ###### Prediction using id3 ##########

    for j in range(1, 6, 2):
        decision_tree_id3 = id3(Xtrn, ytrn, max_depth=j)
        pretty_print(decision_tree_id3)
        ypredicted = [predict_example(x, decision_tree_id3) for x in Xtst]
        confusionmatrix_id3[j] = confusion_matrix(ytst, ypredicted)

        ######## Plotting Trees #########
        dot_string = to_graphviz(decision_tree_id3)
        render_dot_file(dot_string, './UCI_dataset_learn_id3-' + str(j))

    for k in confusionmatrix_id3:
        print("------------------------------------------------------------------------------------------------------------------")
        print("Winsconsin breast cancer : id3 : Depth -> " + str(k) + " : Confusion Matrix")
        print(confusionmatrix_id3[k])
        print("------------------------------------------------------------------------------------------------------------------")

    ########   Prediction using Scikit-learn ####

    # Data_names_v = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']
    Data_names_new = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']

    for j in range(1, 6, 2):
        Classifier = DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=j, min_samples_leaf=5)
        decisiontree_skl = Classifier.fit(Xtrn, ytrn)
        plot_tree(decisiontree_skl)
        ypredicted = decisiontree_skl.predict(Xtst)
        confusionmatrix_scikit[j] = confusion_matrix(ytst, ypredicted)

        ####### Plotting Trees #########
        dot_data_str_2 = tree.export_graphviz(decisiontree_skl, out_file=None, feature_names= Data_names_new, filled=True, rounded=True, special_characters=True)
        graph_skl_2 = pydotplus.graph_from_dot_data(dot_data_str_2)
        graph_skl_2.write_png('UCI_dataset_learn_sklearn-' + str(j) + '.png')
        #Image(filename='UCI_dataset_learn_sklearn-' + str(j) + '.png')

    for k in confusionmatrix_scikit:
        print("------------------------------------------------------------------------------------------------------------------")
        print("Winsconsin breast cancer :  scikit-learn : Depth -> " + str(k) + ": Confusion Matrix")
        print(confusionmatrix_scikit[k])
        print("------------------------------------------------------------------------------------------------------------------")

##########################################################################  END  CODE  LINE  ###########################################################################

