#!/usr/bin/env python

from nav_msgs.srv import GetPlan
from nav_msgs.msg import *
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import Bool, Int16, Header, Float32, String
import rospy
import threading
import logging
import math
import time
import numpy as np
import csv
from math import cos, sin, radians

time_publish_list = []
linear_vel_list = []
angular_vel_list = []

###########################################################################################

def point_pub():
   rospy.init_node('point_pub')
   pub_1 = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=5)
   pub_2 = rospy.Publisher('/flag_value', Int16, queue_size=5)
   rate = rospy.Rate(0.5) # 0.5Hz

   angular_th = 0.0445
   linear_th = 0.025

   #############################################################################

   input_file = "data_files/distAng.csv"
   anglist = []
   distlist = []

   with open(input_file, "rb") as pos_input:
       csv_reader = csv.reader(pos_input)
       csv_reader.next()
       for row in csv_reader:
           angle = float(row[1])
           distance = float(row[2])
           anglist.append(angle)
           distlist.append(distance)


   ##############################################################################

   #flag = 0
   twist = Twist()

   for i in range(0, len(anglist), 1):

       print ("----angle----", anglist[i])

       if (abs(int(anglist[i])) <= 90):

           twist.linear.x = (distlist[i] * 50 * linear_th)
           twist.linear.y = 0.0
           twist.linear.z = 0.0
           twist.angular.x = 0.0
           twist.angular.y = 0.0
           twist.angular.z = (anglist[i] * angular_th)

           print ("-inside 1st if---angle----", anglist[i])

           rospy.loginfo(twist)
           time_publish_list.append(time.time())
           linear_vel_list.append((distlist[i] * 50 * linear_th ))
           angular_vel_list.append((anglist[i] * angular_th))
           pub_1.publish(twist)
           rate.sleep()
           time.sleep(3)

           #flag = flag + 1
           rospy.loginfo(flag)
           pub_2.publish(flag)

       elif (abs(int(anglist[i])) > 90):

           if (anglist[i] >= 0):
               sign = 1
           else:
               sign = -1

           angle_new = abs(int(anglist[i]))
           num = int(angle_new / 90)
           rem = (angle_new % 90)

           print ("-inside 2nd if---angle----", angle_new)
           print ("-inside 2nd if---num----", num)
           print ("-inside 2nd if---rem----", rem)

           twist.linear.x = (distlist[i] * 10)
           twist.linear.y = 0.0
           twist.linear.z = 0.0
           twist.angular.x = 0.0
           twist.angular.y = 0.0
           twist.angular.z = sign*(rem * angular_th)

           rospy.loginfo(twist)
           time_publish_list.append(time.time())
           linear_vel_list.append((distlist[i] * 5))
           angular_vel_list.append((rem*sign*angular_th))
           pub_1.publish(twist)
           rate.sleep()
           time.sleep(3)

           for j in range(0, num, 1):

               twist.linear.x = 0.0
               twist.linear.y = 0.0
               twist.linear.z = 0.0
               twist.angular.x = 0.0
               twist.angular.y = 0.0
               twist.angular.z = sign*(90 * angular_th)

               rospy.loginfo(twist)
               time_publish_list.append(time.time())
               linear_vel_list.append((0.0 * 5))
               angular_vel_list.append((90*sign * angular_th))
               pub_1.publish(twist)
               rate.sleep()
               print ("-inside forloop j----", j)
               time.sleep(3)

           #flag = flag + 1
           rospy.loginfo(flag)
           pub_2.publish(flag)


##################################################################

if __name__ == '__main__':
     try:
         point_pub()
     except rospy.ROSInterruptException:
         pass

     filehandle = open("data_files/linear_speed_angular_speed_data.csv", "w")
     writer = csv.writer(filehandle)
     writer.writerow(["linear_speed", "angular_speed", "time_stamp"])
     for i in range(len(time_publish_list)):
         x = linear_vel_list[i]
         y = angular_vel_list[i]
         z = time_publish_list[i]
         writer.writerow([x, y, z])
     filehandle.close()
