from multiprocessing import Process
import csv
import time
from config import Robo_mov_file_path, Mov_time_file_path

#########################################

def robo_time_write_csv(myData):
    file_path = Mov_time_file_path
    print("----writing data to csv file------")
    myFile = open(file_path, 'ab')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)


###########################################

def Movement_module(file_path):

    task_count = 1
    while True:
        with open(file_path, "r") as f:
            reader = csv.reader(f, delimiter=",")
            data = list(reader)
            row_count = len(data)

        if (row_count != 1):

            for i in range(0, len(data), 1):
                if (i == task_count):
                    extra_time_store = []
                    mov_start_time = time.time()
                    temp = data[i]
                    robot_x = int(temp[2])
                    robot_y = int(temp[3])
                    obj_x = int(temp[4])
                    obj_y = int(temp[5])
                    mov_x = obj_x - robot_x
                    mov_y = (obj_y - robot_y) + 1
                    print ("--- robot going to pick the object ---")
                    for j in range(0, mov_y, 1):
                        print ("----robot--moving----")
                        time.sleep(1)
                    for k in range(0, mov_x, 1):
                        print ("----robot--moving----")
                        time.sleep(1)
                    print ("----robot reached to pick the object-----")
                    task_count = task_count + 1
                    print ("----robot picking the object ----")
                    time.sleep(5)

                    ###########################################################

                    with open(file_path, "r") as f:
                        reader = csv.reader(f, delimiter=",")
                        data = list(reader)
                        row_count = len(data)

                    if (row_count > task_count):
                        data[i][2] = obj_x
                        data[i][3] = obj_y + 1
                        extra_time_store.append(mov_start_time)

                    else:
                        print ("-----robot moving to home or drop location ----")
                        for l in range(0, mov_x, 1):
                            print ("----robot--moving----")
                            time.sleep(1)
                        for j in range(0, mov_y, 1):
                            print ("----robot--moving----")
                            time.sleep(1)
                        print ("-------robot reached home or drop location ----")
                        mov_end_time = time.time()

                    if (len(extra_time_store) == 0):
                        write_data = [[temp[0], temp[1], mov_start_time, mov_end_time]]
                        robo_time_write_csv(write_data)

                    else:
                        for i in range(0, len(extra_time_store), 1):
                            write_data = [[temp[0], temp[1], extra_time_store[i], mov_end_time]]
                            robo_time_write_csv(write_data)

                        write_data = [[temp[0], temp[1], mov_start_time, mov_end_time]]
                        robo_time_write_csv(write_data)



                ###########################################################
###########################################################################

if __name__ == "__main__":

    file_path = Robo_mov_file_path
    p1 = Process(target=Movement_module, args=(file_path, ))
    p1.start()