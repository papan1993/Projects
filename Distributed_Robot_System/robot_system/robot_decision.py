from config import robots_pos, min_aisle_dist, min_rack_dist, Robot_self_name, Robo_mov_file_path
from operator import itemgetter
import time
import csv

def robo_movement_csv(file_path, myData):
    print("----writing data to csv file------")
    myFile = open(file_path, 'ab')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

def decision(product, robots):
    arr_dist = []
    for i in range(0, len(robots), 1):
        temp2 = robots[i][0]
        print temp2
        num = temp2.split("_")
        num_robo = int(num[1])-1
        dist = ((int(product[1])-robots_pos[num_robo][0])*min_aisle_dist) + ((int(product[3])-robots_pos[num_robo][1])*min_rack_dist)
        print dist
        arr_dist.append([temp2, dist])

    arr_dist = sorted(arr_dist, key=itemgetter(1))
    return arr_dist

def robot_work_cal(product, robots, robot_input, start_time, query_end_time, decision_start_time):
    flag = 0

    for i in range(0, len(robots), 1):
        temp = robots[i][0]
        if (Robot_self_name == temp):
            flag = 1
            break

    des_end_time = 0.0

    if (flag == 1):
        des = decision(product, robots)
        print des
        print ("---- robot calculating ultility taking decision -----")
        file_path = Robo_mov_file_path

        if (des[0][0] == Robot_self_name):
            des_end_time = time.time()
            print ("--- I --- " + str(des[0][0]) + "----- executing the task ----")
            print ("\n")
            robo_x = robots_pos[0][0]
            robo_y = robots_pos[0][1]
            obj_x = int(product[1])
            obj_y = int(product[3])
            robo_data = [[robot_input, Robot_self_name, robo_x, robo_y, obj_x, obj_y]]
            robo_movement_csv(file_path, robo_data)
            return True, start_time, query_end_time, decision_start_time, des_end_time

        else:
            des_end_time = time.time()
            print ("------ " + str(des[0][0]) + "----- executing the task ----")
            return False, start_time, query_end_time, decision_start_time, des_end_time

    else:
        des_end_time = time.time()
        print ("---- I ---- " + str(Robot_self_name) + "---- cannot execute the work ----")
        return False, start_time, query_end_time, decision_start_time, des_end_time
