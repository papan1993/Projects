import numpy as np
import brian2 as br
from matplotlib import pyplot as plt

def check_obstacle(test_dataset_dict, test_net, prev_spike_count,
        neuron_labels, input_fig, iteration_no):
    ax = input_fig.gca()
    ax.imshow(test_dataset_dict['x'][iteration_no])
    input_fig.canvas.draw()
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
    v_thresh_e = 'v > ' + str(v_thresh_e)
    reset_e = 'v = v_reset_e'
    max_delay_ie = 10.0*br.ms
    input_delay = 350*br.ms
    resting_delay = 150*br.ms
    total_delay = input_delay + resting_delay
	#num_test = test_dataset_dict['y'].shape[0]
	#prev_spike_count = np.zeros(num_e)
	#test_results = list()
    rate_arr = (test_dataset_dict['x'][iteration_no] / 4).flatten() * br.Hz
    #input_group.rates = rate_arr
    test_net.set_states({'inp':{'rates': rate_arr}})
    test_net.run(total_delay, report = 'text')
    cumulative_spike_count = test_net.get_states()['ex_mon']['count']
    cur_spike_count = np.copy(cumulative_spike_count - prev_spike_count)
    prev_spike_count = np.copy(cumulative_spike_count)
    max_spiking_neuron = str(np.argmax(cur_spike_count))
    #For key press. can change the image with a timer also.
    #ss = input()
    return (neuron_labels[str(max_spiking_neuron)], prev_spike_count)
