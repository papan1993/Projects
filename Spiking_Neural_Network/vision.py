""" Prerequisites : 1) MNIST Dataset inside a folder called MNIST
                    2) Neuron Mapping and Weight Files pickled after training. """

import gzip
import pickle
import numpy as np
import brian2 as br
from struct import unpack
from scipy.stats import mode
from matplotlib import pyplot as plt
import copy


def filter_dict(dataset_dict, filter_set):
    filtered_indices = [i for i, val in enumerate(dataset_dict['y']) if val in filter_set]
    dataset_dict['x'] = dataset_dict['x'][filtered_indices]
    dataset_dict['y'] = dataset_dict['y'][filtered_indices]
    return dataset_dict

def read_mnist(data, labels):
    #Goto the first byte of data.
    data.seek(0)
    #Read Meta Data of images as Unsigned Integer Bytes according to IDX. 
    magic_num = unpack('>I', data.read(4))[0]
    num_images = unpack('>I', data.read(4))[0]
    num_rows = unpack('>I', data.read(4))[0]
    num_cols = unpack('>I', data.read(4))[0]
    metadata_string = ("Magic Number of IDX : {} \n"
                       "No of Images in IDX : {} \n"
                       "No of Rows in IDX : {} \n"
                       "No of Columns in IDX : {}")
    metadata_string = metadata_string.format(magic_num, num_images, num_rows, num_cols)
    print(metadata_string)
    labels.seek(0)
    #Skip test labels magic number.
    labels.read(4)
    num_labels = unpack('>I', labels.read(4))[0]
    #Read all images in a single go.
    total_img_bytes = num_images * num_rows * num_cols
    data_arr = np.asarray(unpack('>' + 'B'*total_img_bytes, data.read(total_img_bytes)))
    data_arr = data_arr.reshape((num_images, num_rows, num_cols))
    #Can do stacking and other image preprocessing for performance(normalization, mean subtraction..).
    #Read labels into an array.
    total_label_bytes = num_images * 1
    labels_arr = np.asarray(unpack('>' + 'B' * total_label_bytes, labels.read(total_label_bytes)))
    dataset_dict = {'x': data_arr, 'y': labels_arr}
    return dataset_dict

def init_vision():
     mnist_path = "/home/dighanchal/Documents/SNN_vision_based_navigation/MNIST/"
     filter_set = {0,1}
     test_data = gzip.open(mnist_path + "t10k-images-idx3-ubyte.gz", "rb")
     test_labels = gzip.open(mnist_path + "t10k-labels-idx1-ubyte.gz", "rb")
     #Read Train and Test data into dicts.
     test_dataset_dict = read_mnist(test_data, test_labels)
     test_dataset_dict = filter_dict(test_dataset_dict, filter_set)
     print("test_data_dict",test_dataset_dict)

     print("No of entries in test set " + str(test_dataset_dict['y'].shape[0]))
     print("Unique Entries with Count : " + str(np.unique(test_dataset_dict['y'], return_counts=True)))
     del test_data, test_labels
     neuron_label_map = pickle.load(open("/home/dighanchal/Documents/SNN_vision_based_navigation/MNIST/neuron_map.pickle", "rb"))
     neuron_labels = dict()
     for key, value in neuron_label_map.items():
         neuron_labels[key] = mode(value)[0][0]
     print(np.unique(np.array(list(neuron_labels.values())), return_counts=True))
     training_weights = pickle.load(open("//home/dighanchal/Documents/SNN_vision_based_navigation/MNIST/cur_weights.pickle", "rb"))
     #Excitatory Neuron General Equation.
     v_rest_e = -65
     v_thresh_e = -52
     v_reset_e = -65
     refrac_e = 5*br.ms
     tau_e = 100*br.ms
     #Equilibrium Potentials of excitatory and inhibitory synapses for excitatory neuron.
     e_equi_e = 0.0
     e_equi_i = -100
     #Time constant of synaptic conductance.
     tau_g_e = 1.0*br.ms
     tau_g_i = 2.0*br.ms
     excitatory_eqn = ''' dv/dt = ((v_rest_e - v) + (I_syn_e + I_syn_i)) / tau_e : 1 (unless refractory)
                          I_syn_e = g_e*(e_equi_e - v) : 1
                          I_syn_i = g_i*(e_equi_i - v) : 1
                         dg_e/dt = -g_e/tau_g_e : 1 (unless refractory)
                          dg_i/dt = -g_i/tau_g_i : 1 (unless refractory) '''
     num_e = 400
     v_thresh_e = 'v > ' + str(v_thresh_e)
     reset_e = 'v = v_reset_e'
     ex_group = br.NeuronGroup(num_e, excitatory_eqn, threshold=v_thresh_e, reset=reset_e, refractory=refrac_e, name='ex')
     ex_group.v = v_rest_e
     ex_monitor = br.SpikeMonitor(ex_group, name = 'ex_mon')
     num_input = 784
     max_delay_ie = 10.0*br.ms
     input_group = br.PoissonGroup(num_input, 0 * br.Hz, name = 'inp')
     input_monitor = br.SpikeMonitor(input_group, name = 'inp_mon')
     non_stdp_syn = br.Synapses(input_group, ex_group, model = 'w : 1', on_pre='g_e_post += w', name = 'inp_ex_syn')
     non_stdp_syn.connect()
     non_stdp_syn.w = training_weights
     non_stdp_syn.delay = 'rand()*max_delay_ie'
     test_net = br.Network(input_group, ex_group, non_stdp_syn, ex_monitor)
     input_fig = plt.figure()
     ax = input_fig.gca()
     ax.get_xaxis().set_visible(False)
     ax.get_yaxis().set_visible(False)
     input_fig.show()
     return (test_dataset_dict, test_net, neuron_labels, input_fig, num_e)

"""
def init_vision():
    mnist_path = "/home/dighanchal/Documents/SNN_vision_based_navigation/MNIST/"
    filter_set = {0}
    test_data = gzip.open(mnist_path + "t10k-images-idx3-ubyte.gz", "rb")
    test_labels = gzip.open(mnist_path + "t10k-labels-idx1-ubyte.gz", "rb")
    # Read Train and Test data into dicts.
    dict_1 = read_mnist(test_data, test_labels)
    dict_2 = copy.deepcopy(dict_1)
    dict_1 = filter_dict(dict_1, filter_set)
    filter_set = {1}
    dict_2 = filter_dict(dict_2, filter_set)
    #print("dict1", dict_1)
    #print("dict2", dict_2)

    test_dataset_dict =  dict()
    test_dataset_dict = {'x': dict_1['x'][:10]}
    test_dataset_dict['y'] = dict_1['y'][:10]
    test_dataset_dict['x'] = np.append(test_dataset_dict['x'], dict_2['x'][:10], axis=0)
    test_dataset_dict['y'] = np.append(test_dataset_dict['y'], dict_2['y'][:10], axis=0)
    test_dataset_dict['x'] = np.append(test_dataset_dict['x'], dict_1['x'][:10], axis=0)
    test_dataset_dict['y'] = np.append(test_dataset_dict['y'], dict_1['y'][:10], axis=0)
    test_dataset_dict['x'] = np.append(test_dataset_dict['x'], dict_2['x'][:5], axis=0)
    test_dataset_dict['y'] = np.append(test_dataset_dict['y'], dict_2['y'][:5], axis=0)
    test_dataset_dict['x'] = np.append(test_dataset_dict['x'], dict_1['x'][:10], axis=0)
    test_dataset_dict['y'] = np.append(test_dataset_dict['y'], dict_1['y'][:10], axis=0)

    print ("test_dataset_dict:", test_dataset_dict)
    print("No of entries in test set " + str(test_dataset_dict['y'].shape[0]))
    print("Unique Entries with Count : " + str(np.unique(test_dataset_dict['y'], return_counts=True)))
    del test_data, test_labels
    neuron_label_map = pickle.load(
        open("/home/dighanchal/Documents/SNN_vision_based_navigation/MNIST/neuron_map.pickle", "rb"))
    neuron_labels = dict()
    for key, value in neuron_label_map.items():
        neuron_labels[key] = mode(value)[0][0]
    print(np.unique(np.array(list(neuron_labels.values())), return_counts=True))
    training_weights = pickle.load(
        open("//home/dighanchal/Documents/SNN_vision_based_navigation/MNIST/cur_weights.pickle", "rb"))
    # Excitatory Neuron General Equation.
    v_rest_e = -65
    v_thresh_e = -52
    v_reset_e = -65
    refrac_e = 5 * br.ms
    tau_e = 100 * br.ms
    # Equilibrium Potentials of excitatory and inhibitory synapses for excitatory neuron.
    e_equi_e = 0.0
    e_equi_i = -100
    # Time constant of synaptic conductance.
    tau_g_e = 1.0 * br.ms
    tau_g_i = 2.0 * br.ms
    excitatory_eqn = ''' dv/dt = ((v_rest_e - v) + (I_syn_e + I_syn_i)) / tau_e : 1 (unless refractory)
                         I_syn_e = g_e*(e_equi_e - v) : 1
                         I_syn_i = g_i*(e_equi_i - v) : 1
                         dg_e/dt = -g_e/tau_g_e : 1 (unless refractory)
                         dg_i/dt = -g_i/tau_g_i : 1 (unless refractory) '''
    num_e = 400
    v_thresh_e = 'v > ' + str(v_thresh_e)
    reset_e = 'v = v_reset_e'
    ex_group = br.NeuronGroup(num_e, excitatory_eqn, threshold=v_thresh_e, reset=reset_e, refractory=refrac_e,
                              name='ex')
    ex_group.v = v_rest_e
    ex_monitor = br.SpikeMonitor(ex_group, name='ex_mon')
    num_input = 784
    max_delay_ie = 10.0 * br.ms
    input_group = br.PoissonGroup(num_input, 0 * br.Hz, name='inp')
    input_monitor = br.SpikeMonitor(input_group, name='inp_mon')
    non_stdp_syn = br.Synapses(input_group, ex_group, model='w : 1', on_pre='g_e_post += w', name='inp_ex_syn')
    non_stdp_syn.connect()
    non_stdp_syn.w = training_weights
    non_stdp_syn.delay = 'rand()*max_delay_ie'
    test_net = br.Network(input_group, ex_group, non_stdp_syn, ex_monitor)
    input_fig = plt.figure()
    ax = input_fig.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    input_fig.show()
    return (test_dataset_dict, test_net, neuron_labels, input_fig, num_e)
"""

if __name__ == '__main__':
    init_vision()