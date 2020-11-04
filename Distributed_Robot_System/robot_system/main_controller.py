import sys
from query_module import Query_search, query_main
from robot_explore import explore
from robot_decision import robot_work_cal
import time
import zmq
import csv
from config import Input_csv_path, Robot_self_name, Time_store_file_path

#########################################

def robo_time_write_csv(file_path, myData):
    print("----writing data to csv file------")
    myFile = open(file_path, 'ab')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

#############################################################

def csv_reader(file_obj):

    reader = csv.reader(file_obj)
    task_queue = []
    num = 0

    for row in reader:
        if (num != 0):
            task_queue.append(row[1])
        num = num +1

    return task_queue

#################################################################

def controller(robot_input, start_time):

    print (' ------ Robot input------ ', robot_input)
    query_res = Query_search(robot_input)    ##### query - 1
    product = []
    robots = []

    if (query_res == False):
        print ('--- robot start exploration -----')
        explore_res = explore(robot_input)   ##### query - 2

        if (explore_res == False):
            print (" ------ no object found of that kind ----- ")


        else:
            print ("---- Again searching for the details of object in the warehouse -----")
            search_2 = Query_search(robot_input)  ##### query - 3

            if (search_2 == False):
                print ("---- Object not found ------")


            else:
                time.sleep(10)
                product, robots = query_main(robot_input)  ##### query - 4

    else:
        print ('------ result output -------------')
        product, robots = query_main(robot_input) ##### query - 2

    ###################################################################################
    robot_query_end_time = time.time()
    #######################################
    robot_decision_start_time = time.time()

    if (robots == None):
        des_end_time = time.time()
        print ("----- Nothing found no task can be executed -------")


    else:
        print ("---- decising the task -----")
        exe_res, start_time, query_end_time, decision_start_time, des_end_time = robot_work_cal(product, robots, robot_input, start_time, robot_query_end_time, robot_decision_start_time)

        if (exe_res == True):
            print ("--------object will be delivered at destination--------")

        else:
            print ("------object fail to deliver at the destination------")

    ###########################

    net_time = [[robot_input, Robot_self_name, start_time, query_end_time, decision_start_time, des_end_time]]
    robo_time_write_csv(Time_store_file_path, net_time)


#############################

if __name__ == '__main__':

######################################################

    csv_path = Input_csv_path
    task_queue = []

    with open(csv_path, "rb") as f_obj:
        task_queue = csv_reader(f_obj)

    for i in range(0, len(task_queue), 1):
        task_main = task_queue[i]
        print ("-------Starting a New Task ---------")
        task_start_time = time.time()
        controller(str(task_main), task_start_time)


#########################################################