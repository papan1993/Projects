#!/usr/bin/env python
import roslib
import rospy
import time
import csv
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool, Int16, Header, Float32, String

xlist = []
ylist = []
flag = 0
flag2 = 1
time_list = []
#time_now = 0
#time_later = 0

def store_val(val_x, val_y, time_ts):

    print("----position--- X -----", val_x)
    print("----position--- Y -----", val_y)
    print("----timestamp--- time stamp ----", time_ts)
    xlist.append(val_x)
    ylist.append(val_y)
    time_list.append(time_ts)

######################################################################

def flag_node(data):
    global flag
    flag = data.data

######################################################################

def position_node(msg):

    global flag
    global flag2
#    global time_now
#    global time_later
#    time_later = time.time()
#    diff = (time_now - time_later)
#    diff = round(diff)

#    if (diff == 1):
#        store_val(msg.pose.pose.position.x, msg.pose.pose.position.y, time.time())
#        time_now = time_later

    if (flag2 == flag):
        print("------ Destination Reached No ----", flag2)
        store_val(msg.pose.pose.position.x, msg.pose.pose.position.y, time.time())
        flag2 = flag2 + 1


######################################################################

if __name__ == "__main__":
#    global time_now
#    global time_later
    rospy.init_node('odometry_node', anonymous=True)
    rospy.Subscriber('/odom', Odometry, position_node)
    rospy.Subscriber('/flag_value', Int16, flag_node)
#    time_now = time.time()
    rospy.spin()

    filehandle = open("data_files/excel_data/robot_XY_coordinates.csv", "w")
    writer = csv.writer(filehandle)
    writer.writerow(["x", "y", "time_stamp"])
    for i in range(len(xlist)):
        x = xlist[i]
        y = ylist[i]
        z = time_list[i]
        writer.writerow([x, y, z])
    filehandle.close()
