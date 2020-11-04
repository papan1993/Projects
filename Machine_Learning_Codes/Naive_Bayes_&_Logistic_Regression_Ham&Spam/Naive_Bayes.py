#!/usr/bin/env python

import glob

################### global variables #############
main_data = {'ham':[],'spam':[]}
output_list = []
stop_word_list = ['a','about','above','after','again','against','all','am','an','and','any','are',"aren't",'as','at','be','because','been','before','being','below','between','both','but','by',"can't",'cannot','could',"couldn't",'did',"didn't",'do',"does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's",'hers','herself',"him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into",'is',"isn't",'it',"it's",'its',"itself","let's",'me','more','most',"mustn't",'my','myself','no','nor','not','of','off','on','once','only',"or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've",'this','those','through','to','too','under','until','up','very','was',"wasn't",'we',"we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's",'with',"won't","would","wouldn't",'you',"you'd","you'll","you're","you've",'your','yours','yourself','yourselves']

##########################################  Getting Training and Testing main_data ##############

#### Retrive training and testing files ####
def get_train_files(ham_path, spam_path):
    ham_files = glob.glob(ham_path)
    spam_files = glob.glob(spam_path)

    return ([ham_files,spam_files])

def get_test_files(ham_path, spam_path):
    test_ham_files = glob.glob(ham_path)
    test_spam_files = glob.glob(spam_path)

    return ([test_ham_files,test_spam_files])

######### Retrive ham and spam data ######
def get_spam_data(spam_files):

    global main_data
    unique_spam = []

    for spam in spam_files:
        spam_words = []
        try:
            with open(spam, encoding="utf8", errors='ignore') as file2:
                spam_words = [each_word for line in file2 for each_word in line.split()]

        except OSError as ex:
            print(ex.message)

        finally:
            if len(spam_words) > 0:
                main_data['spam'] += spam_words
                unique_spam += list(set(spam_words))
                unique_spam = list(set(unique_spam))

    return (unique_spam)

def get_ham_data(ham_files):

    global main_data
    unique_ham = []

    for ham in ham_files:
        ham_words = []
        try:
           with open(ham, encoding="utf8",errors='ignore') as file1:
               ham_words = [each_word for line in file1 for each_word in line.split()]

        except OSError as ex:
            print(ex.message)

        finally:
            if len(ham_words) > 0:
                main_data['ham'] += ham_words
                unique_ham += list(set(ham_words))
                unique_ham = list(set(unique_ham))

        return unique_ham

####### retrive ham and spam data with stop words #####
def get_spam_data_with_stopwords(spam_files):
    global main_data
    unique_spam = []

    for spam in spam_files:
        spam_words = []
        try:
            with open(spam, encoding="utf8", errors='ignore') as file2:

                for line in file2:
                    for each_word in line.split():
                        if each_word not in stop_word_list:
                            spam_words.append(each_word)

        except OSError as ex:
            print(ex.message)

        finally:
            if len(spam_words) > 0:
                main_data['spam'] += spam_words
                unique_spam += list(set(spam_words))
                unique_spam = list(set(unique_spam))

    return (unique_spam)

def get_ham_data_with_stopwords(ham_files):

    global main_data
    unique_ham = []

    for ham in ham_files:
        ham_words = []
        try:
           with open(ham, encoding="utf8",errors='ignore') as file1:

            for line in file1:
                for each_word in line.split():
                    if each_word not in stop_word_list:
                        ham_words.append(each_word)

        except OSError as ex:
            print(ex.message)

        finally:
            if len(ham_words) > 0:
                main_data['ham'] += ham_words
                unique_ham += list(set(ham_words))
                unique_ham = list(set(unique_ham))

        return unique_ham

################### Append spam and ham ########

def vocab_train_list(unique_spam, unique_ham):

    vocab_list = list(set(unique_spam + unique_ham))
    return vocab_list

############################ Stat for ham and spam ###############################

def ham_stats(unique_ham):

    global main_data
    ham_dict = {}

    for i in unique_ham:
        if (ham_dict.get(i) == None):
            ham_dict[i]=0
        ham_dict[i]+=main_data['ham'].count(i)

    return ham_dict

def spam_stats(unique_spam):

    global main_data
    spam_dict = {}

    for i in unique_spam:
        if (spam_dict.get(i) == None):
            spam_dict[i] = 0
        spam_dict[i] += main_data['spam'].count(i)

    return spam_dict

############################# find unique words #####################################

def retrieve_unique(word_list):
    ret = list(set(word_list))
    return ret

############################### predict ham and spam #########################################

def predict_ham(word_list, ham, vocab):

    unique_word_list = retrieve_unique(word_list)
    prob_cal = 0

    for each_word in unique_word_list:
        prob_cal = (word_list.count(each_word)+1)/(len(ham)+len(vocab))

    return prob_cal

def predict_spam(word_list, spam, vocab):

    unique_word_list = retrieve_unique(word_list)
    prob_cal = 0

    for each_word in unique_word_list:
        prob_cal = (word_list.count(each_word)+1)/(len(spam)+len(vocab))

    return prob_cal


def predict_ham_spam(wordlist, ham, spam, vocab):

    pred_result = {}
    pred_result['spam'] = predict_spam(wordlist, spam, vocab)
    pred_result['ham'] = predict_ham(wordlist, ham, vocab)

    if (pred_result['spam'] > pred_result['ham']):
        pred_result['prediction'] = 'spam'
    else:
        pred_result['prediction'] = 'ham'

    return pred_result

##################### Compute Test Ham and Spam Prediction ###########################################

########### Spam ##########
def test_spam_prediction(test_spamfiles, ham, spam, vocab):

    global output_list

    for test_spam in test_spamfiles:
        test_spam_words = []
        try:
           with open(test_spam, encoding="utf8",errors='ignore') as file1:
               test_spam_words = [test_word  for line in file1 for test_word in line.split()]

        except OSError as ex:
            print(ex.message)

        finally:
            if len(test_spam_words) > 0:
                    output_dict = {}
                    output_dict['predicted'] = predict_ham_spam(test_spam_words, ham, spam, vocab)
                    output_dict['actual'] = 'spam'

            output_list.append(output_dict)

##################### Ham ########
def test_ham_prediction(test_hamfiles, ham, spam, vocab):

    global output_list

    for test_ham in test_hamfiles:
        test_ham_words = []
        try:
           with open(test_ham, encoding="utf8",errors='ignore') as file2:
               test_ham_words = [test_word for line in file2 for test_word in line.split()]

        except OSError as ex:
            print(ex.message)

        finally:
            if len(test_ham_words) > 0:
                output_dict = {}
                output_dict['predicted'] = predict_ham_spam(test_ham_words, ham, spam, vocab)
                output_dict['actual'] = 'ham'

            output_list.append(output_dict)

############### Compute accuracy ###############################################

def compute_Accuracy(output_list):

    correct_val = 0
    error_val = 0

    for pred in output_list:
        if (pred.get('predicted').get('prediction') == pred.get('actual')):
            correct_val = correct_val +  1
        else:
            error_val = error_val + 1

    accuracy = (correct_val*100/(correct_val + error_val))

    return accuracy

########################   Main Operation Functions  ###########

######### Without Stop Word List #########
def main_operation(train_file_path_ham, train_file_path_spam, test_file_path_ham, test_file_path_spam):

    [ham_files, spam_files] = get_train_files(train_file_path_ham, train_file_path_spam)
    unique_ham = get_ham_data(ham_files)
    unique_spam = get_spam_data(spam_files)

    vocab = vocab_train_list(unique_spam, unique_ham)
    spam_stat = spam_stats(unique_spam)
    ham_stat = ham_stats(unique_ham)

    [test_hamfiles,test_spamfiles] = get_test_files(test_file_path_ham, test_file_path_spam)
    test_ham_prediction(test_hamfiles, ham_stat, spam_stat, vocab)
    test_spam_prediction(test_spamfiles, ham_stat, spam_stat, vocab)

    global output_list
    acc = compute_Accuracy(output_list)
    print(' Naive Bayes : Predictions Accuracy without stop word -> ', acc)

######### With Stop Word List #########
def main_operation_stopword(train_file_path_ham, train_file_path_spam, test_file_path_ham, test_file_path_spam):

    [ham_files,spam_files] = get_train_files(train_file_path_ham, train_file_path_spam)
    unique_ham = get_ham_data_with_stopwords(ham_files)
    unique_spam = get_spam_data_with_stopwords(spam_files)

    vocab = vocab_train_list(unique_spam, unique_ham)
    spam_stat = spam_stats(unique_spam)
    ham_stat = ham_stats(unique_ham)

    [test_hamfiles,test_spamfiles] = get_test_files(test_file_path_ham, test_file_path_spam)
    test_ham_prediction(test_hamfiles, ham_stat, spam_stat, vocab)
    test_spam_prediction(test_spamfiles, ham_stat, spam_stat, vocab)

    global output_list
    acc = compute_Accuracy(output_list)
    print(' Naive Bayes : Predictions Accuracy with stop word -> ', acc)

##### starting main ######
if __name__=="__main__":

    train_file_path_ham = './train//ham/*'
    train_file_path_spam = './train//spam/*'

    test_file_path_ham = './test//ham/*'
    test_file_path_spam = './test//spam/*'

    main_operation(train_file_path_ham, train_file_path_spam, test_file_path_ham, test_file_path_spam)
    main_operation_stopword(train_file_path_ham, train_file_path_spam, test_file_path_ham, test_file_path_spam)