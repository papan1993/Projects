from __future__ import division
from __future__ import print_function

import numpy as np
import torch
import shutil
import gzip
from decimal import Decimal
import json

#from pygcn.pruning_algorithm_inference import load_ckp
#from pygcn.train_pruning import load_ckp

def extract_binary_code(value, identify_key, data_type):
    bin_form = bin(value)
    bin_strip = str(bin_form).lstrip("0b")
    if identify_key is None:
        final_bin_form = bin_strip
    else:
        final_bin_form = str(identify_key) + bin_strip

    final_bin_form = int(final_bin_form, 2)
    #final_bin_form = data_type(final_bin_form)
    final_bin_form = torch.as_tensor(final_bin_form, dtype=data_type)
    return final_bin_form

def repeat_calculate(count_frequency, max_count, upper_freq_threshold):
    num_val = 0
    for i in range(0, max_count, 1):
        temp = count_frequency[i]
        if temp > upper_freq_threshold:
            num_val = num_val + 1
    return num_val

def compute_no_bits(count_frequency, max_count):
    num_bits = 0
    min_bits_threshold = 4
    max_bits_threshold = 14   ### because no.of bits gives n + 1
    upper_freq_threshold = 5
    change_threshold = 2
    num_val = 0

    while num_bits < min_bits_threshold:
        num_val = repeat_calculate(count_frequency, max_count, upper_freq_threshold)
        rem = pow(2, num_bits)
        while num_val >= rem:
            num_bits = num_bits + 1
            rem = pow(2, num_bits)
        upper_freq_threshold = upper_freq_threshold - change_threshold

    while num_bits > max_bits_threshold:
        upper_freq_threshold = upper_freq_threshold + change_threshold
        num_val = repeat_calculate(count_frequency, max_count, upper_freq_threshold)
        rem = pow(2, num_bits)
        while num_val >= rem:
            num_bits = num_bits + 1
            rem = pow(2, num_bits)

    if pow(2, num_bits) == num_val:
        final_num_bits = num_bits
    else:
        final_num_bits = num_bits - 1   ### Lower Bound
    return final_num_bits

def max_num_bits(value):
    start = 0
    cal = pow(2, start)
    while value >= cal:
        start = start + 1
        cal = pow(2, start)

    if value == cal:
        return start
    else:
        return start + 1

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

def compression_module(model, compression_type, sensitivity):

    global store_value_data_type
    dictionary_data_codebook = {}

    if sensitivity == 'High':
        store_value_data_type = torch.float64
    elif sensitivity == 'Medium':
        store_value_data_type = torch.float32
    elif sensitivity == 'Low':
        store_value_data_type = torch.float16

    for name, param in model.named_parameters():

        name_split = name.split(".")
        layer_type = name_split[1]

        if layer_type == 'weight':

            layer_data = param.data.numpy()
            #dim_arr_x = layer_data.shape[0]
            #dim_arr_y = layer_data.shape[1]

            unique_weights, count_frequency = np.unique(layer_data, return_counts=True)
            #print("unique values -->   ", unique_weights, count_frequency)

            ######### Compute the number of bits #############

            len_count_freq = len(count_frequency)

            number_of_bits = compute_no_bits(count_frequency, len_count_freq)
            number_dict_index = int(pow(2, number_of_bits))
            remaining_elements = len_count_freq - number_dict_index

            ########## Compute remaining bits ##########
            rem_bits = max_num_bits(remaining_elements)

            indices = np.argpartition(count_frequency, -number_dict_index)[-number_dict_index:]
            weights_index_dict = unique_weights[indices]
            #print("test --> ", unique_weights[indices])

            ################## Typecasting and compression values ###########

            data_type = {'float_16': torch.float16, 'float_32': torch.float32, 'int_32': torch.int32, 'int_16': torch.int16,
                         'int_8': torch.int8, 'int_8_u': torch.uint8}

            #store_value_data_type = data_type['float_16']
            if compression_type == 1:
                if number_of_bits > 7:
                    casebook_data_type = data_type['int_16']
                elif number_of_bits > 15:
                    casebook_data_type = data_type['int_32']
                else:
                    casebook_data_type = data_type['int_8_u']

                if rem_bits > 7:
                    huff_data_type = data_type['int_16']
                elif rem_bits > 15:
                    huff_data_type = data_type['int_32']
                else:
                    huff_data_type = data_type['int_8_u']

            else:
                if number_of_bits > 8:
                    casebook_data_type = data_type['int_16']
                elif number_of_bits > 16:
                    casebook_data_type = data_type['int_32']
                else:
                    casebook_data_type = data_type['int_8_u']

                if rem_bits > 8:
                    huff_data_type = data_type['int_16']
                elif rem_bits > 16:
                    huff_data_type = data_type['int_32']
                else:
                    huff_data_type = data_type['int_8_u']

            # if (number_of_bits > rem_bits):
            #     final_data_type = casebook_data_type
            # else:
            #     final_data_type = huff_data_type

            final_data_type = store_value_data_type

            #layer_buf_table = np.empty(layer_data.shape, dtype=object)
            #layer_buf_table = np.empty(layer_data.shape)
            layer_buf_table = torch.empty(layer_data.shape)
            layer_dictionary_data = {}
            identification_bit = {0: '0', 1: '1', 2: None}

            count_for_freq_values = 0
            count_for_huffman_values = 0
            compare_list = []
            comparison_dict = {}
            approximate_bias = torch.tensor(0.03456, dtype=store_value_data_type)

            bits_list = []
            for i in range(0, pow(2, number_of_bits), 1):
                bits_list.append(float(i))

            if compression_type == 1:

                for i in range(0, len(layer_data), 1):
                    temp = layer_data[i]
                    for j in range(0, len(temp), 1):
                        weight_val = temp[j]

                        weight_val_check = float(weight_val)
                        if (bits_list.count(weight_val_check) >= 0):
                            weight_val = weight_val + approximate_bias


                        compare_freq = np.isin(weight_val, weights_index_dict)
                        if not compare_freq.__bool__():
                            weight_val = torch.as_tensor(weight_val, dtype = store_value_data_type)
                            bit_string = extract_binary_code(count_for_huffman_values, identification_bit[1], huff_data_type)
                            # if len(compare_list) == 0:
                            #     layer_dictionary_data[bit_string] = weight_val
                            #     count_for_huffman_values = count_for_huffman_values + 1
                            #     compare_list.append(weight_val)
                            weight_val_norm = float(weight_val)
                            weight_val_norm = round(weight_val_norm, 3)
                            check = compare_list.count(weight_val_norm)
                            if check == 0:
                                layer_dictionary_data[bit_string] = weight_val
                                count_for_huffman_values = count_for_freq_values + count_for_huffman_values
                                compare_list.append(weight_val_norm)
                                layer_buf_table[i][j] = bit_string
                                comparison_dict[weight_val_norm] = bit_string
                            else:
                                find_bit_string = comparison_dict[weight_val_norm]
                                layer_buf_table[i][j] = find_bit_string
                        else:
                            #weight_val = store_value_data_type(weight_val)
                            weight_val = torch.as_tensor(weight_val, dtype = store_value_data_type)
                            bit_string = extract_binary_code(count_for_freq_values, identification_bit[0], casebook_data_type)
                            # if len(compare_list) == 0:
                            #     layer_dictionary_data[bit_string] = weight_val
                            #     count_for_freq_values = count_for_freq_values + 1
                            #     compare_list.append(weight_val)
                            weight_val_norm = float(weight_val)
                            weight_val_norm = round(weight_val_norm, 3)
                            check = compare_list.count(weight_val_norm)
                            if check == 0:
                                layer_dictionary_data[bit_string] = weight_val
                                count_for_freq_values = count_for_freq_values + 1
                                compare_list.append(weight_val_norm)
                                layer_buf_table[i][j] = bit_string
                                comparison_dict[weight_val_norm] = bit_string
                            else:
                                find_bit_string = comparison_dict[weight_val_norm]
                                layer_buf_table[i][j] = find_bit_string



                print("encoded compression type 1")

            elif compression_type == 0:

                for i in range(0, len(layer_data), 1):
                    temp = layer_data[i]
                    for j in range(0, len(temp), 1):
                        weight_val = temp[j]

                        compare_freq = np.isin(weight_val, weights_index_dict)
                        if not compare_freq.__bool__():
                            #weight_val = store_value_data_type(weight_val)
                            weight_val = torch.as_tensor(weight_val, dtype = store_value_data_type)
                            layer_buf_table[i][j] = weight_val
                        else:
                            #weight_val = store_value_data_type(weight_val)
                            weight_val = torch.as_tensor(weight_val, dtype = store_value_data_type)
                            bit_string = extract_binary_code(count_for_freq_values, identification_bit[0], casebook_data_type)
                            # if len(compare_list) == 0:
                            #     layer_dictionary_data[bit_string] = weight_val
                            #     count_for_freq_values = count_for_freq_values + 1
                            #     compare_list.append(weight_val)
                            weight_val_norm = float(weight_val)
                            weight_val_norm = round(weight_val_norm, 3)
                            check = compare_list.count(weight_val_norm)
                            if check == 0:
                                layer_dictionary_data[bit_string] = weight_val
                                count_for_freq_values = count_for_freq_values + 1
                                compare_list.append(weight_val_norm)
                                layer_buf_table[i][j] = bit_string
                                comparison_dict[weight_val_norm] = bit_string
                            else:
                                find_bit_string = comparison_dict[weight_val_norm]
                                layer_buf_table[i][j] = find_bit_string



                print("encoded compression type 2")

            ########################################### edit later #########

            str_name = str(name).split(".")
            #layer_dict_name_1 = str_name[0] + str('_') + str_name[1] + str('_bufferTable')
            #layer_dict_name_2 = str_name[0] + str('_') + str_name[1] + str('_dictionary')

            layer_dict_name = str_name[0] + str('_') + str_name[1]
            dictionary_data_codebook[layer_dict_name] = layer_dictionary_data
            # compressed_model_array = np.array(layer_buf_table)
            # param.data = torch.from_numpy(compressed_model_array)
            compressed_model_array = torch.as_tensor(layer_buf_table, dtype=final_data_type)
            param.data = compressed_model_array

        elif layer_type == 'bias':

            param.data = torch.as_tensor(param.data, dtype=store_value_data_type)

        #############################
    path= "./model_trained/weight_model_dict_feather.pt"
    path_new = path + str('.gz')
    json_path = "./model_trained/weight_model_dict_feather.json"
    torch.save(dictionary_data_codebook, path)
    with open(json_path, 'w') as fp:
        json.dump(str(dictionary_data_codebook), fp)
    fp.close()
    # with open(path, 'rb') as f_in:
    #     with gzip.open(path_new, 'wb') as f_out:
    #         shutil.copyfileobj(f_in, f_out)
    return model, dictionary_data_codebook, final_data_type

def decode_compression_module(model, optimizer, model_path, dictionary_path, compression_mode):

    Model_inference, optimizer, features, labels, final_data_type = load_ckp(model_path, model, optimizer)

    # with open(dictionary_path) as json_file:
    #     dict_data = json.load(json_file)

    dict_data = torch.load(dictionary_path)

    for name, param in Model_inference.named_parameters():

        name_split = name.split(".")
        layer_type = name_split[1]

        if layer_type == 'weight':

            str_name = str(name).split(".")
            layer_dict_name = str_name[0] + str('_') + str_name[1]
            layer_dict_data = dict_data[layer_dict_name]
            layer_data = param.data

            temp_dict = {}
            for keys, values in layer_dict_data.items():
                keys_n = int(keys)
                temp_dict[keys_n] = values

            len_keys = len(layer_dict_data.keys())
            keys_list = []
            for i in range(0, len_keys, 1):
                keys_list.append(float(i))

            if compression_mode == 1:

                for i in range(0, len(layer_data), 1):
                    temp = layer_data[i]
                    for j in range(0, len(temp), 1):
                        each_block = temp[j]
                        each_block = int(each_block)
                        layer_data[i][j] = temp_dict[each_block]
                        #print("check")

            elif compression_mode == 0:

                for i in range(0, len(layer_data), 1):
                    temp = layer_data[i]
                    for j in range(0, len(temp), 1):
                        each_block = temp[j]
                        each_block_chn = float(each_block)
                        #if (Decimal(each_block_chn) % 1 == 0):
                        if (keys_list.count(each_block_chn) == 1):
                            each_block = int(each_block)
                            layer_data[i][j] = temp_dict[each_block]
                            #print("check")

            param.data = torch.as_tensor(layer_data, dtype=torch.float)
        param.data = torch.as_tensor(param.data, dtype=torch.float)

    print("decoder")
    return Model_inference, optimizer, features, labels, final_data_type
