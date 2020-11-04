import numpy as np
from scipy import math

from config import *

def navigator(ini_pos, ang_target, robot_hdg_ang, snn_direc, sensors_angles, label):
    print("---robot_hdg------>",robot_hdg_ang)
    print("----sensor_angles---->",sensors_angles)
    print("#######################################")
    turn_ang = robot_hdg_ang - ang_target
    turn_ang_abs = abs(turn_ang)

    ########### manual - obtain from robot
    change_ang_degree = (ang_target * 180)/3.14
    tem_cal_cos = math.cos(change_ang_degree)
    #print("tem_cal_cos ---> ", tem_cal_cos)

    next_pt_x = ini_pos[0]
    next_pt_y = ini_pos[1]
    next_hdg = ini_pos[2]

    obs = label
    print("---obs---", obs)
    if obs == 1:
        next_pt_x_r = next_pt_x + 0.25
        dist1 = math.sqrt(((target_pos[0] - next_pt_x_r) * (target_pos[0] - next_pt_x_r)) + (
            (target_pos[1] - next_pt_y) * (target_pos[1] - next_pt_y)))
        next_pt_x_l = next_pt_x - 0.25
        dist2 = math.sqrt(((target_pos[0] - next_pt_x_l) * (target_pos[0] - next_pt_x_l)) + (
            (target_pos[1] - next_pt_y) * (target_pos[1] - next_pt_y)))
        dist = min(dist1, dist2)
        if dist == dist1:  ####right
            next_pt_x = next_pt_x_r
            next_hdg = robot_hdg_ang - math.pi / 2
        else:  #######left
            next_pt_x = next_pt_x_l
            next_hdg = robot_hdg_ang + math.pi / 2
    #next_pt = [next_pt_x, next_pt_y, next_hdg]

    elif obs == 0:
        if (tem_cal_cos == 0):
            next_pt_x = ini_pos[0] + robo_linear_vel
        else:
            next_pt_x = ini_pos[0] + (robo_linear_vel * tem_cal_cos)

        tem_cal_sin = math.sin(change_ang_degree)
        # print("tem_cal_sin ---> ", tem_cal_sin)
        if (tem_cal_sin == 0):
            next_pt_y = ini_pos[1] + robo_linear_vel
        else:
            next_pt_y = ini_pos[1] + (robo_linear_vel * tem_cal_sin)

        next_hdg = np.mod(robot_hdg_ang - turn_ang, math.pi)

    next_pt = [next_pt_x, next_pt_y, next_hdg]






    ########## sensor angle update
    for i in range(len(sensors_angles)):
        if (snn_direc[0] == 1):
            temp = sensors_angles[i] - turn_ang_abs  ### turning right
            sensors_angles[i] = temp

        elif (snn_direc[1] == 1):
            if (robot_hdg_ang > turn_ang):
                temp = sensors_angles[i] - turn_ang_abs
                sensors_angles[i] = np.mod(temp,math.pi)

            elif (robot_hdg_ang < turn_ang):
                temp = sensors_angles[i] + turn_ang_abs
                sensors_angles[i] = np.mod(temp,math.pi)

        elif (snn_direc[2] == 1):
            temp = sensors_angles[i] + turn_ang_abs   ### turning left
            sensors_angles[i] = np.mod(temp,math.pi)
    return next_pt, sensors_angles
