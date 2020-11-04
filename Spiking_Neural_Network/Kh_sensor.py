from config import *

def sensor_module(ang_target, dist, sensors_angles):
    sensor_new_1 = []
    sensor_data = sensors_angles
    #Angle difference between sensor and target.
    for i in range(len(sensor_data)):
        diff = abs(ang_target - sensor_data[i])
        sensor_new_1.append(diff)
    sensor_new_2 = []
    #Normalize.
    max_val = max(sensor_new_1)
    for i in range(len(sensor_new_1)):
        temp = 1 - (sensor_new_1[i]/max_val)
        temp = temp/dist
        sensor_new_2.append(temp)
    return sensor_new_2
