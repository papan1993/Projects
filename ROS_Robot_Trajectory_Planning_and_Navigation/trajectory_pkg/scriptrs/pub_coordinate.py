#!/usr/bin/env python

from nav_msgs.srv import GetPlan
from nav_msgs.msg import *
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool, Int16, Header, Float32, String
import rospy
import threading
import logging
import math
import numpy as np

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

def point_pub():
   pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)
   rospy.init_node('point_pub', anonymous=True)
   #rate = rospy.Rate(10) # 10hz

   ############### ---input---coordinates---- #########

   input_data = []

   tot_data = [['/map', '1', '/map', -1.0, -1.0, 0.01], ['/map', '2', '/map', 1.0, 1.0, 0.01]]

   for i in range(0, len(tot_data), 1):
       goal = MoveBaseActionGoal()
       goal.header.frame_id = "/map"
       goal.goal_id.id = tot_data[i][1]
       goal.goal.target_pose.header.frame_id = "/map"
       goal.goal.target_pose.pose.position.x = tot_data[i][3]
       goal.goal.target_pose.pose.position.y = tot_data[i][4]
       goal.goal.target_pose.pose.position.z = 0.0
       goal.goal.target_pose.pose.orientation.w = 0.01

       input_data.append(goal)

   print("data before publish----", input_data)

   while not rospy.is_shutdown():
       #rospy.loginfo(input_data)
       pub.publish(input_data)
       #rate.sleep()

   #if True:
      #hello_str = "hello world %s" % rospy.get_time()
      #rospy.loginfo(input_data)
      #pub.publish(input_data)
      #rate.sleep()

   #rospy.loginfo(input_data)
   #pub.publish(input_data)
   
if __name__ == '__main__':
     try:
         point_pub()
     except rospy.ROSInterruptException:
         pass
