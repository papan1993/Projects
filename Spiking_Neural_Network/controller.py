import numpy as np
from scipy import math
from matplotlib import pyplot as plt
import pickle
from config import *
from navigation_train import *
from Kh_sensor import *
#from try_1 import *
from try_2 import *
from vision import init_vision
from obstacle_avoidance import check_obstacle


def distance_cal(ini_pos, targ_pos):
    diff_x = (ini_pos[0] - targ_pos[0]) * (ini_pos[0] - targ_pos[0])
    diff_y = (ini_pos[1] - targ_pos[1]) * (ini_pos[1] - targ_pos[1])
    val = math.sqrt((diff_x + diff_y))
    return val

############################

def angle_cal(ini_pos, targ_pos):
    diff_x = (targ_pos[0] - ini_pos[0])
    diff_y = (targ_pos[1] - ini_pos[1])
    var = math.atan2(diff_y, diff_x)
    return var

###########################

def main_controller():
    #Initializing Visual Pipeline. 
    test_dataset_dict, test_net, neuron_labels, input_fig, num_e = init_vision()
    prev_spike_count = np.zeros(num_e)
    prev_nav_spike = np.zeros(3)
    test_results = list()

    num_test = test_dataset_dict['y'].shape[0]
    print("No of Test Entries : ", num_test)
    #Values from config file.
    ini_pos = initial_pos
    targ_pos = target_pos
    robot_hdg_ang = ini_pos[2]
    sensors_angles = [ang_sensor_1, ang_sensor_2, ang_sensor_3]
    print("---initial point --> ", ini_pos)
    print("\n")
    print("################################################################")
    print("\n")
    count = 0
    net = snn_navigation()
    #Create the output figure.
    output_fig = plt.figure()
    plt.xlim(0,20)
    plt.ylim(0,20)
    output_fig.show()
    while not ((abs(ini_pos[0] - target_pos[0]) <= 0.40) and (abs(ini_pos[1] - target_pos[1]) <= 0.40)):
        #Plot output images and wait till enter.
        out_ax = output_fig.gca()
        out_ax.plot(ini_pos[0], ini_pos[1], 'ro')
        out_ax.plot(targ_pos[0], targ_pos[1], 'ko')
        output_fig.canvas.draw()
        #gg = input()
        #Get each frame and check for obstacle.
        label, prev_spike_count = check_obstacle(test_dataset_dict, test_net, prev_spike_count, neuron_labels, input_fig, count)    
        test_results.append(label)
        print("count---> ", count)
        dist = distance_cal(ini_pos, targ_pos)
        print("dist-> ",dist)
        ang_target = angle_cal(ini_pos, targ_pos)
        sensor_data = sensor_module(ang_target, dist, sensors_angles)
        snn_spike_data, nav_weight, prev_nav_spike  = direc_selector(net, sensor_data, prev_nav_spike)
        print("snn-spike -> ", snn_spike_data)
        next_pt, sensors_angles_new = navigator(ini_pos, ang_target, robot_hdg_ang, snn_spike_data, sensors_angles, label)
        ini_pos = next_pt
        robot_hdg_ang = ini_pos[2]
        sensors_angles = sensors_angles_new
        count = count + 1
        print("---next point --> ", ini_pos)
        print("\n")
        print("################################################################")
        print("\n")
    #Close the plots and calculate the overall accuracy.
    plt.close()
    with open("final_weights_navigation.pickle", 'wb') as final_weight_file:
        pickle.dump(nav_weight, final_weight_file)

    test_results = np.array(test_results)
    print("No of Test Cases: " + str(num_test))
    #print("No of Correct Classifications : " + str(np.count_nonzero(test_results == test_dataset_dict['y'][:num_test])))
  ########################

if __name__ == '__main__':
    main_controller()
    print("Done")
