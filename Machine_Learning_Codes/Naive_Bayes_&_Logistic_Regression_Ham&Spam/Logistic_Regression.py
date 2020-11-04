#!/usr/bin/env python

import numpy as np
import pandas as pd
import codecs
import os
import warnings

warnings.filterwarnings("ignore")
stop_words_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do',"does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's",'hers','herself',"him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into",'is',"isn't",'it',"it's",'its',"itself","let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only',"or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've",'this','those','through','to','too','under','until','up','very','was',"wasn't",'we',"we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's",'with',"won't","would","wouldn't",'you',"you'd","you'll","you're","you've",'your','yours','yourself','yourselves']

########################## Split test and training data ############################

def Train_and_Test_Data_Split(train_dir_in, test_dir_in):
    
    train_data = dict()
    test_data = dict()

    spam_add_path = '/spam'
    ham_add_path = '/ham'
    
    train_data['spam'] = os.listdir(train_dir_in + spam_add_path)
    train_data['ham'] = os.listdir(train_dir_in + ham_add_path)

    test_data['spam'] = os.listdir(test_dir_in + spam_add_path)
    test_data['ham'] = os.listdir(test_dir_in + ham_add_path)

    return train_data, test_data

################## Generate tokens ################

def Gen_Tokens_list(text_input):
    
    tokens_all = text_input.strip().split()

    for i in range(0, len(tokens_all)-1, 1):
        tokens_all += tokens_all[i] + ' ' + tokens_all[i + 1]

    tokens_temp = set(tokens_all)
    tokens_temp = list(tokens_temp)

    dataframe_num = pd.DataFrame({'col':tokens_temp})
    dataframe_num.col = pd.Categorical(dataframe_num.col)
    dataframe_num['code'] = dataframe_num.col.cat.codes
    temp_code = dataframe_num.code
    return_value = list(temp_code)

    return return_value

######################################

def Delete_Stop_Words(text_input):

    delete_list = []
    tokens_all = text_input.strip().split()

    for i in range(0, len(tokens_all)-1, 1):
        tokens_all += tokens_all[i] + ' ' + tokens_all[i + 1]

    tokens_temp = set(tokens_all)

    for each_token in tokens_temp:
        if (each_token not in stop_words_list):
            delete_list.append(each_token)

    delete_list_temp = list(delete_list)

    dataframe_num = pd.DataFrame({'col':delete_list_temp})
    dataframe_num.col = pd.Categorical(dataframe_num.col)
    dataframe_num['code'] = dataframe_num.col.cat.codes
    temp_code = dataframe_num.code
    return_value = list(temp_code)

    return return_value

############################ Logistic Training Function #########

def Logistic_with_Stopwords(train_val, train_direc):

    token_BOW = []
    weight = np.zeros((1,161))
    bias = np.zeros((1,1))
    lr = 10
    alpha = 0.1

    for delim, last_str in list(train_val.items()):

        for each_str in last_str:
            with codecs.open(train_direc +'/'+ delim + '/'+ each_str, "r",encoding='utf-8', errors='ignore') as file1:
                token_BOW = token_BOW + Gen_Tokens_list(file1.read())

                each_x = np.array(token_BOW)
                if delim == 'spam':
                    y_res = 1
                else:
                    y_res = 0

                weight_shape = np.shape(each_x)
                weight = np.arange(1*weight_shape[0]).reshape(1, weight_shape[0]).astype(float)
                bias = np.zeros((1,weight_shape[0])).astype(float)
                each_x = each_x.astype(float)

                for epoch in range(0, 500, 1):

                    z_temp = (weight * each_x) + bias
                    x_exp = 1 / (1 + np.e**(-z_temp))
                    y_res = np.arange(1 * weight_shape[0]).reshape(1,weight_shape[0])
                    err_val = (-y_res * np.log(x_exp) + (1-y_res) * np.log(1-x_exp))
                    L2_val = (err_val) + (lr/2) + (np.square(weight))
                    update_weight = (np.array(alpha * L2_val).astype(float)) - ((np.array(alpha * lr) *weight).astype(float))
                    weight = weight + update_weight

    return weight

#######################################################################

def Logistic_without_Stopwords(train_val, train_direc):

    token_BOW = []
    weight = np.zeros((1,161))
    bias = np.zeros((1,1))
    lr = 10
    alpha = 0.1

    for delim, last_str in list(train_val.items()):

        for each_str in last_str:
            with codecs.open(train_direc +'/'+ delim + '/'+ each_str, "r",encoding='utf-8', errors='ignore') as file2:
                token_BOW = token_BOW + Gen_Tokens_list(file2.read())

                each_x = np.array(token_BOW)
                if delim == 'spam':
                    y_res = 1
                else:
                    y_res = 0

                weight_shape = np.shape(each_x)
                weight = np.arange(1 * weight_shape[0]).reshape(1, weight_shape[0]).astype(float)
                bias = np.zeros((1, weight_shape[0])).astype(float)
                each_x = each_x.astype(float)
                
                for epoch in range(0, 500, 1):
                    
                    z_temp = (weight * each_x) + bias
                    x_exp = 1 / (1 + np.e**(-z_temp))
                    y_res = np.arange(1 * weight_shape[0]).reshape(1, weight_shape[0])
                    error_val = (-y_res * np.log(x_exp) + (1-y_res) * np.log(1-x_exp))
                    L2_val = (error_val) + (lr/2) + (np.square(weight))
                    update_weight = (np.array(alpha * L2_val).astype(float)) - ((np.array(alpha * lr) * weight).astype(float))
                    weight = weight + update_weight

    return weight

##################### Testing the spam and ham training #########

def test_with_Stopwords(test_val, test_direc, trained_weight):

    token_bow = []
    net_Count = 0
    total_Correct_Count = 0

    for each_class, each_list in list(test_val.items()):
        count_correct_class = 0

        for each_word in each_list:
            with codecs.open(test_direc + '/' + each_class + '/' + each_word, "r", encoding='utf-8', errors='ignore') as file1:
                token_bow = token_bow + Delete_Stop_Words(file1.read())

                x_in = np.array(token_bow).astype(float)
                in_shape = np.shape(x_in)
                trained_weight = np.arange(1 * in_shape[0]).reshape(1, in_shape[0])
                trained_weight = trained_weight.astype(float)
                bias = np.zeros((1, in_shape[0])).astype(float)

                z_cal = (np.matmul(trained_weight, x_in))
                prob_cal = np.e**(z_cal) / (1 + np.e**(z_cal))

                if (prob_cal > 0.5):
                    predict_class = 'spam'
                else:
                    predict_class = 'ham'

                if predict_class == each_class:
                    count_correct_class = count_correct_class + 1

            net_Count = net_Count + 1

        total_Correct_Count = total_Correct_Count + count_correct_class

    accuracy = (float(total_Correct_Count) / net_Count) * float(100)
    return accuracy

###########################################################################

def test_without_Stopwords(test_val, test_direc, trained_weight):

    token_bow = []
    net_Count = 0
    total_Correct_Count = 0

    for each_class, each_list in list(test_val.items()):
        count_correct_class = 0

        for each_word in each_list:
            with codecs.open(test_direc + '/' + each_class + '/'+ each_word, "r",encoding='utf-8', errors='ignore') as file2:
                token_bow = token_bow + Delete_Stop_Words(file2.read())

                x_in = np.array(token_bow).astype(float)
                in_shape = np.shape(x_in)
                trained_weight = np.arange(1 * in_shape[0]).reshape(1, in_shape[0])
                trained_weight = trained_weight.astype(float)
                bias = np.zeros((1, in_shape[0])).astype(float)

                z_cal = (np.matmul(trained_weight, x_in))
                prob_cal = np.e**(z_cal) / (1 + np.e**(z_cal))

                if(prob_cal > 0.5):
                     predict_class = 'spam'
                else:
                    predict_class = 'ham'

                if predict_class == each_class:
                    count_correct_class = count_correct_class + 1

            net_Count = net_Count + 1

        total_Correct_Count = total_Correct_Count + count_correct_class

    accuracy = (float(total_Correct_Count) / net_Count) * float(100)
    return accuracy

######################## Main function ######################

def main_function(main_train_dir, main_test_dir):

    train_data, test_data = Train_and_Test_Data_Split(main_train_dir, main_test_dir)

    ########### without stop words ######
    trained_weight = Logistic_without_Stopwords(train_data, main_train_dir)
    test_data_acc = test_without_Stopwords(test_data, main_test_dir, trained_weight)
    print("Accuracy without stop words:", test_data_acc)

    ########### with stop words ######
    trained_weight_withstp = Logistic_with_Stopwords(train_data, main_train_dir)
    test_data_withstp_acc = test_with_Stopwords(test_data, main_test_dir, trained_weight_withstp)
    print("Accuracy with stop words:", test_data_withstp_acc)
    
if __name__ == '__main__':

    main_train_dir = "./train"
    main_test_dir = "./test"
    print(" Logistic Regression Model : SPAM and HAM data ", "\n", " CODE IS RUNNING ", "\n", " IT WILL TAKE APPROX 15 - 20 MINUTES  ... ")
    main_function(main_train_dir, main_test_dir)





