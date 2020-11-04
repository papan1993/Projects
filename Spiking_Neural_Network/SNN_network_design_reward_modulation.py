import numpy as np
import pickle
from random import randint
from brian2 import *

def snn_navigation():

    ##################  Number of neurons #####################

    num_inputs_main = 1
    num_inputs = 2
    num_inputs_hidden = 5

    ###############  sensor_inputs ###############

    sensor_input_1 = [2, 6]
    sensor_input_2 = [1, 4]
    sensor_input_3 = [3, 1]
    distance_target = [20, 12]
    angle_target = [30, 4]
    reward = [50, -20]

    ############  input neuron groups  ############

    P1 = PoissonGroup(num_inputs_main, 0*Hz, name='nav_inp_s1')
    P2 = PoissonGroup(num_inputs_main, 0*Hz, name='nav_inp_s2')
    P3 = PoissonGroup(num_inputs_main, 0*Hz, name='nav_inp_s3')
    P4 = PoissonGroup(num_inputs_main, 0*Hz, name='nav_inp_dis')
    P5 = PoissonGroup(num_inputs_main, 0*Hz, name='nav_inp_ang')

    ###########  neuron group monitor ###############

    MP1 = SpikeMonitor(P1)
    MP2 = SpikeMonitor(P2)
    MP3 = SpikeMonitor(P3)
    MP4 = SpikeMonitor(P4)
    MP5 = SpikeMonitor(P5)

    ################  LIF neuron model and equation with time constants  ######

    tau = 10 * ms
    Wmax = 5
    Wmin = -5
    Wmax_hid = 10
    Wmin_hid = -10

    ########################### Synaptic parameters ####################

    tau_pre = tau_post = 10 * ms
    Apre = 0.2
    Apost = -0.2
    wmin = 0
    wmax = 10.0
    e_dynamic = 0
    tau_z = 10 * ms
    lr = 0.5
    r = randint(0, 10)

    ################### dummy eqn replace by LIF  ##################

    eqs = '''
       dv/dt = -v/tau : 1
       '''

    #################   Input layers - inhibitory and exhibitory layers  ################

    I_1_ex = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_ex_1')
    I_1_inh = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_inh_1')
    I_2_ex = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_ex_2')
    I_2_inh = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_inh_2')
    I_3_ex = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_ex_3')
    I_3_inh = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_inh_3')
    I_4_ex = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_ex_4')
    I_4_inh = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_inh_4')
    I_5_ex = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_ex_5')
    I_5_inh = NeuronGroup(num_inputs, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_input_inh_5')

    ##############################  STDP connection between sensors input and input layer  #######################


    Syn_input_ex1 = Synapses(P1, I_1_ex, model =' w : 1', on_pre ='v += w', name = 'syn_inp_ex_1')
    Syn_input_ex1.connect()
    Syn_input_ex1.w = 'rand()*Wmax'
    Syn_input_inh1 = Synapses(P1, I_1_inh, model =' w : 1', on_pre ='v += w', name = 'syn_inp_inh_1')
    Syn_input_inh1.connect()
    Syn_input_inh1.w = 'rand()*Wmin'

    Syn_input_ex2 = Synapses(P2, I_2_ex, model =' w : 1', on_pre ='v += w', name = 'syn_inp_ex_2')
    Syn_input_ex2.connect()
    Syn_input_ex2.w = 'rand()*Wmax'
    Syn_input_inh2 = Synapses(P2, I_2_inh, model =' w : 1', on_pre ='v += w', name = 'syn_inp_inh_2')
    Syn_input_inh2.connect()
    Syn_input_inh2.w = 'rand()*Wmin'

    Syn_input_ex3 = Synapses(P3, I_3_ex, model =' w : 1', on_pre ='v += w', name = 'syn_inp_ex_3')
    Syn_input_ex3.connect()
    Syn_input_ex3.w = 'rand()*Wmax'
    Syn_input_inh3 = Synapses(P3, I_3_inh, model =' w : 1', on_pre ='v += w', name = 'syn_inp_inh_3')
    Syn_input_inh3.connect()
    Syn_input_inh3.w = 'rand()*Wmin'

    Syn_input_ex4 = Synapses(P4, I_4_ex, model =' w : 1', on_pre ='v += w', name = 'syn_inp_ex_4')
    Syn_input_ex4.connect()
    Syn_input_ex4.w = 'rand()*Wmax'
    Syn_input_inh4 = Synapses(P4, I_4_inh, model =' w : 1', on_pre ='v += w', name = 'syn_inp_inh_4')
    Syn_input_inh4.connect()
    Syn_input_inh4.w = 'rand()*Wmin'

    Syn_input_ex5 = Synapses(P5, I_5_ex, model =' w : 1', on_pre ='v += w', name = 'syn_inp_ex_5')
    Syn_input_ex5.connect()
    Syn_input_ex5.w = 'rand()*Wmax'
    Syn_input_inh5 = Synapses(P5, I_5_inh, model =' w : 1', on_pre ='v += w', name = 'syn_inp_inh_5')
    Syn_input_inh5.connect()
    Syn_input_inh5.w = 'rand()*Wmin'

    #################   Hidden layers - inhibitory and exhibitory layers  ################

    ############   STDP equations  ##################

    syn_eqn_main = ''' e_dynamic : 1
                       dapre/dt = -apre/tau_pre : 1 (clock-driven)
                       dapost/dt = -apost/tau_post : 1 (clock-driven)
                       dP_plus/dt = (- P_plus + apre)/tau_pre : 1 (clock-driven)
                       dP_minus/dt = (- P_minus + apost)/tau_post : 1 (clock-driven)
                       dEligib_z/dt = (- Eligib_z + e_dynamic) / tau_z : 1 (clock-driven)
                       w : 1
                       r : 1'''

    syn_pre_E = ''' apre += Apre
                  e_dynamic += P_minus
                  w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
                  v_post = v_post + w + r'''

    syn_pre_I = ''' apre += Apre
                  e_dynamic += P_minus
                  w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
                  v_post = v_post + w - r'''

    syn_post = ''' apost += Apost
                   e_dynamic += P_plus
                   w = clip((w + (apre*Eligib_z))*lr), Wmin, Wmax)
                   v_post = v_post + w '''

    ##########################################

    # syn_pre = ''' apre += Apre
    #               e_dynamic += P_minus
    #               w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
    #               v_post = v_post + w '''
    #

    ################################

    # syn_post_I_I = ''' apost += Apost
    #                e_dynamic += P_plus
    #                w = clip((w + (apre*Eligib_z))*lr), Wmin, Wmax)
    #                v_post = v_post + w - r'''



    # syn_post_I_E = ''' apost += Apost
    #                e_dynamic += P_plus
    #                w = clip((w + (apre*Eligib_z))*lr), Wmin, Wmax)
    #                v_post = v_post + w + r'''

    # syn_pre_E_I = ''' apre += Apre
    #               e_dynamic += P_minus
    #               w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
    #               v_post = v_post + w - r'''

    # syn_post_E_I = ''' apost += Apost
    #                e_dynamic += P_plus
    #                w = clip((w + (apre*Eligib_z))*lr), Wmin, Wmax)
    #                v_post = v_post + w - r'''

    # syn_pre_E_E = ''' apre += Apre
    #               e_dynamic += P_minus
    #               w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
    #               v_post = v_post + w + r'''

    # syn_post_E_E = ''' apost += Apost
    #                e_dynamic += P_plus
    #                w = clip((w + (apre*Eligib_z))*lr), Wmin, Wmax)
    #                v_post = v_post + w + r'''


    ##############################################################

    G_ex = NeuronGroup(num_inputs_hidden, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_hidden_ex')
    G_inh = NeuronGroup(num_inputs_hidden, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_hidden_inh')


    #################   Input layers to hidden layers connection  ################

    Syn_hidden_ex1 = Synapses(I_1_ex, G_ex, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_ex_1')
    Syn_hidden_ex1.connect()
    Syn_hidden_ex1.w = 'rand()*Wmax_hid'
    Syn_hidden_ex2 = Synapses(I_1_inh, G_ex, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_ex_2')
    Syn_hidden_ex2.connect()
    Syn_hidden_ex2.w = 'rand()*Wmax_hid'
    Syn_hidden_ex3 = Synapses(I_2_ex, G_ex, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_ex_3')
    Syn_hidden_ex3.connect()
    Syn_hidden_ex3.w = 'rand()*Wmax_hid'
    Syn_hidden_ex4 = Synapses(I_2_inh, G_ex, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_ex_4')
    Syn_hidden_ex4.connect()
    Syn_hidden_ex4.w = 'rand()*Wmax_hid'
    Syn_hidden_ex5 = Synapses(I_3_ex, G_ex, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_ex_5')
    Syn_hidden_ex5.connect()
    Syn_hidden_ex5.w = 'rand()*Wmax_hid'
    Syn_hidden_ex6 = Synapses(I_3_inh, G_ex, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_ex_6')
    Syn_hidden_ex6.connect()
    Syn_hidden_ex6.w = 'rand()*Wmax_hid'
    Syn_hidden_ex7 = Synapses(I_4_ex, G_ex, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_ex_7')
    Syn_hidden_ex7.connect()
    Syn_hidden_ex7.w = 'rand()*Wmax_hid'
    Syn_hidden_ex8 = Synapses(I_4_inh, G_ex, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_ex_8')
    Syn_hidden_ex8.connect()
    Syn_hidden_ex8.w = 'rand()*Wmax_hid'
    Syn_hidden_ex9 = Synapses(I_5_ex, G_ex, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_ex_9')
    Syn_hidden_ex9.connect()
    Syn_hidden_ex9.w = 'rand()*Wmax_hid'
    Syn_hidden_ex10 = Synapses(I_5_inh, G_ex, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_ex_10')
    Syn_hidden_ex10.connect()
    Syn_hidden_ex10.w = 'rand()*Wmax_hid'

    Syn_hidden_inh1 = Synapses(I_1_ex, G_inh, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_inh_1')
    Syn_hidden_inh1.connect()
    Syn_hidden_inh1.w = 'rand()*Wmin_hid'
    Syn_hidden_inh2 = Synapses(I_1_inh, G_inh, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_inh_2')
    Syn_hidden_inh2.connect()
    Syn_hidden_inh2.w = 'rand()*Wmin_hid'
    Syn_hidden_inh3 = Synapses(I_2_ex, G_inh, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_inh_3')
    Syn_hidden_inh3.connect()
    Syn_hidden_inh3.w = 'rand()*Wmin_hid'
    Syn_hidden_inh4 = Synapses(I_2_inh, G_inh, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_inh_4')
    Syn_hidden_inh4.connect()
    Syn_hidden_inh4.w = 'rand()*Wmin_hid'
    Syn_hidden_inh5 = Synapses(I_3_ex, G_inh, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_inh_5')
    Syn_hidden_inh5.connect()
    Syn_hidden_inh5.w = 'rand()*Wmin_hid'
    Syn_hidden_inh6 = Synapses(I_3_inh, G_inh, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_inh_6')
    Syn_hidden_inh6.connect()
    Syn_hidden_inh6.w = 'rand()*Wmin_hid'
    Syn_hidden_inh7 = Synapses(I_4_ex, G_inh, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_inh_7')
    Syn_hidden_inh7.connect()
    Syn_hidden_inh7.w = 'rand()*Wmin_hid'
    Syn_hidden_inh8 = Synapses(I_4_inh, G_inh, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_inh_8')
    Syn_hidden_inh8.connect()
    Syn_hidden_inh8.w = 'rand()*Wmin_hid'
    Syn_hidden_inh9 = Synapses(I_5_ex, G_inh, model = syn_eqn_main, on_pre = syn_pre_E, on_post= syn_post, name = 'syn_hidden_inh_9')
    Syn_hidden_inh9.connect()
    Syn_hidden_inh9.w = 'rand()*Wmin_hid'
    Syn_hidden_inh10 = Synapses(I_5_inh, G_inh, model = syn_eqn_main, on_pre = syn_pre_I, on_post= syn_post, name = 'syn_hidden_inh_10')
    Syn_hidden_inh10.connect()
    Syn_hidden_inh10.w = 'rand()*Wmin_hid'

    #################   Output layers  ################

    Output_left = NeuronGroup(num_inputs_main, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_output_left')
    Output_right = NeuronGroup(num_inputs_main, eqs, threshold ='v>1', reset ='v=0.1', name = 'nav_output_right')

    ############################## STDP section - hidden layer - output layer  #####################

    ############   STDP equations  ##################

    syn_eqn_main_f = ''' e_dynamic : 1
                       dapre/dt = -apre/tau_pre : 1 (clock-driven)
                       dapost/dt = -apost/tau_post : 1 (clock-driven)
                       dP_plus/dt = (- P_plus + apre)/tau_pre : 1 (clock-driven)
                       dP_minus/dt = (- P_minus + apost)/tau_post : 1 (clock-driven)
                       dEligib_z/dt = (- Eligib_z + e_dynamic) / tau_z : 1 (clock-driven)
                       w : 1
                       r : 1'''

    syn_pre_I_f = ''' apre += Apre
                  e_dynamic += P_minus
                  w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
                  v_post = v_post + w - r'''

    syn_pre_E_f = ''' apre += Apre
                  e_dynamic += P_minus
                  w = clip((w + (apost*Eligib_z))*lr), Wmin, Wmax)
                  v_post = v_post + w + r'''

    syn_post_f = ''' apost += Apost
                   e_dynamic += P_plus
                   w = clip((w + (apre*Eligib_z))*lr), Wmin, Wmax)
                   v_post = v_post + w '''

    ##########################################

    #################   Output layers - synapses   ################

    Syn_hidden_ex_output_left = Synapses(G_ex, Output_left, model = syn_eqn_main_f, on_pre = syn_pre_E_f, on_post = syn_post_f, name = 'output_left_ex')
    Syn_hidden_ex_output_left.connect()
    Syn_hidden_ex_output_left.w = 'rand()*Wmax'

    Syn_hidden_ex_output_right = Synapses(G_ex, Output_right, model = syn_eqn_main_f, on_pre = syn_pre_E_f, on_post = syn_post_f, name = 'output_right_ex')
    Syn_hidden_ex_output_right.connect()
    Syn_hidden_ex_output_right.w = 'rand()*Wmax'

    Syn_hidden_inh_output_left = Synapses(G_inh, Output_left, model = syn_eqn_main_f, on_pre = syn_pre_I_f, on_post = syn_post_f, name = 'output_left_inh')
    Syn_hidden_inh_output_left.connect()
    Syn_hidden_inh_output_left.w = 'rand()*Wmin'

    Syn_hidden_inh_output_right = Synapses(G_inh, Output_right, model = syn_eqn_main_f, on_pre = syn_pre_I_f, on_post = syn_post_f, name = 'output_right_inh')
    Syn_hidden_inh_output_right.connect()
    Syn_hidden_inh_output_right.w = 'rand()*Wmin'

    ################################################################################################################







    ######################################################################################################

    #######################################  Dummy Code  ###########################################

    Syn_exin = Synapses(G_ex, G_inh, model =' w : 1', on_pre ='v_post += w', name = 'nav_syn_exin')
    Syn_exin.connect(j='i')
    Syn_exin.w = 10.4

    Syn_inex = Synapses(G_inh, G_ex, model =' w : 1', on_pre ='v_post += -w', name = 'nav_syn_inex')
    Syn_inex.connect(condition ='i != j')
    Syn_inex.w = 12

    S = Synapses(P, G_ex, model =' w : 1', on_pre ='v += w', name ='nav_syn')
    S.connect()
    M = SpikeMonitor(G_ex, name='spike_ex')
    max_init_weight_ie = 0.5
    S.w = '(rand() + 0.001)*max_init_weight_ie'
    #with open("final_weights_navigation_train.pickle", 'wb') as final_weight_file:
     #   pickle.dump(np.array(S.w), final_weight_file)

    #training_nav_weight = pickle.load(open("//home/dighanchal/Documents/SNN_vision_based_navigation/final_weights_navigation.pickle", "rb"))
    #S.w = training_nav_weight
    net = Network(P, G_ex, G_inh, Syn_exin, Syn_inex, S, M)


    ###############################  STDP equations for Reward ##########################

    lr = 0.05 #### learning rate
    # rd = 10 #### update the reward for each event

    ########### Stimuli section - using Poisson Group  #######################

    eqn = ''' v : 1 '''

    num_inputs = 2
    input_rate = 100 * Hz

    P = PoissonGroup(num_inputs, rates=input_rate)
    G = NeuronGroup(num_inputs, eqn, threshold='v >= 1.0', reset='v = 0.1')

    syn_eqn_main = ''' e_dynamic : 1
                       dapre/dt = -apre/tau_pre : 1 (clock-driven)
                       dapost/dt = -apost/tau_post : 1 (clock-driven)
                       dP_plus/dt = (- P_plus + apre)/tau_pre : 1 (clock-driven)
                       dP_minus/dt = (- P_minus + apost)/tau_post : 1 (clock-driven)
                       dEligib_z/dt = (- Eligib_z + e_dynamic) / tau_z : 1 (clock-driven)
                       w : 1 '''

    syn_pre = ''' apre += Apre
                  e_dynamic += P_minus
                  w = clip((w + (apost*Eligib_z))*lr), wmin, wmax)
                  v_post = v_post + w '''

    syn_post = ''' apost += Apost
                   e_dynamic += P_plus
                   w = clip((w + (apre*Eligib_z))*lr), wmin, wmax)
                   v_post = v_post + w '''

    ########### STDP section #############################

    Syn = Synapses(P, G, model=syn_eqn_main, on_pre=syn_pre, on_post=syn_post, method='euler')
    # Full connectivity.
    Syn.connect()

    Syn.apost = 0.4

    ################ Reward Modulated ####################

    # dopamine_indices = array([0, 0, 0])
    # dopamine_times = array([3520, 4020, 4520])*ms
    # dopamine = SpikeGeneratorGroup(1, dopamine_indices, dopamine_times)
    # dopamine_monitor = SpikeMonitor(dopamine)

    # reward_on_pre = '''V_post += epsilon_dopa'''

    # reward = Synapses(dopamine, synapse_stdp, model='''''', on_pre=reward_on_pre, method='exact')
    # reward.connect()

    #####################################################

    #################################################################################

    return net

def direc_selector(net, sensor_data, prev_nav_spike):
    tau = 10 * ms
    input_rate1 = (sensor_data[0] * 10000)
    input_rate2 = (sensor_data[1] * 10000)
    input_rate3 = (sensor_data[2] * 10000)
    net.set_states({'nav_inp': {'rates': [input_rate1, input_rate2, input_rate3] * Hz }})
    net.run(1 * second)

    spike_count = net.get_states()['spike_ex']['count']
    curr_nav_weights = np.array(net.get_states()['nav_syn']['w'])
    print("current_weights>>>",curr_nav_weights)
    cur_spike_count = np.copy(spike_count - prev_nav_spike)
    prev_nav_spike = np.copy(spike_count)

    max_to_spike = np.argmax(spike_count)
    #first_to_spike = spike_count.index(max(spike_count))
    snn_spike = [0, 0, 0]
    snn_spike[max_to_spike] = 1
    return snn_spike, curr_nav_weights, prev_nav_spike


def snn_brian_simulator(sensor_data):
    #start_scope()
    print("sensor data---> ", sensor_data)
    num_inputs = 3
    input_rate1 = (sensor_data[0] * 10000)
    input_rate2 = (sensor_data[1] * 10000)
    input_rate3 = (sensor_data[2] * 10000)

    P = PoissonGroup(num_inputs, [input_rate1, input_rate2, input_rate3] * Hz)
    MP = SpikeMonitor(P)

    #tau = 10 * ms
    #dummy eqn replace by LIF
    eqs = '''
    dv/dt = -v/tau : 1
    '''
    G_ex = NeuronGroup(num_inputs, eqs, threshold='v>1', reset='v=0')
    G_inh = NeuronGroup(num_inputs, eqs, threshold='v>1', reset='v=0')

    Syn_exin = Synapses(G_ex, G_inh, model=' w : 1', on_pre='v_post += w')
    Syn_exin.connect(j='i')
    Syn_exin.w = 10.4

    Syn_inex = Synapses(G_inh, G_ex, model=' w : 1', on_pre='v_post += -w')
    Syn_inex.connect(condition='i != j')
    Syn_inex.w = 12

    S = Synapses(P, G_ex, model=' w : 1', on_pre='v += w')
    S.connect()
    M = SpikeMonitor(G_ex)
    state_M = StateMonitor(G_ex,'v', record= True)
    max_init_weight_ie = 0.5
    S.w = '(rand() + 0.001)*max_init_weight_ie'

    # Store the current state of the network
    net = Network(P, G_ex, G_inh, Syn_exin, Syn_inex, S, M)
    #net.store()
    net.run(1 * second)

    #spike_dict = M.spike_trains()
    spike_count = M.num_spikes
    spikes_1 = M.count[0]  # with unit
    print("spike_count1>>>", spikes_1)

    spikes_2 = M.count[1]  # with units
    print("spike_count2>>>", spikes_2)
    #

    spikes_3 = M.count[2]  # with units
    print("spike_count3>>>", spikes_3)

    spike_counts = [spikes_1, spikes_2, spikes_3]
    first_to_spike = spike_counts.index(max(spike_counts))
    snn_spike = [0, 0, 0]
    snn_spike[first_to_spike] = 1
    #with open("final_weights"+str(count)+".pickle", 'wb') as final_weight_file:
    #pickle.dump(np.array(S.w), final_weight_file)

    return snn_spike, np.array(S.w)

