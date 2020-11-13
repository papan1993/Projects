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

#def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

#def listener():
#    rospy.init_node('listener', anonymous=True)
#    rospy.Subscriber("chatter", String, callback)
#    rospy.spin()

def point_pub():
   rospy.init_node('point_pub')
   pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=5)   
   rate = rospy.Rate(0.5) # 10hz

   angular_speed = 0.65 # w/s
   linear_speed = 0.15  # m/s

   ############### ---input---coordinates---- #########

   #input_data = []

   #tot_data = [['/map', '1', '/map', -1.0, -1.0, 0.01], ['/map', '2', '/map', 1.0, 1.0, 0.01]]

   twist = Twist()
   twist.linear.x = 0.2
   twist.linear.y = 0.0
   twist.linear.z = 0.0
   twist.angular.x = 0.0
   twist.angular.y = 0.0
   twist.angular.z = 0.0

#   rospy.loginfo(twist)
#   pub.publish(twist)

   while not rospy.is_shutdown():
       rospy.loginfo(twist)
       pub.publish(twist)
       rate.sleep()
       time.sleep(5)
  
if __name__ == '__main__':
     try:
         point_pub()
     except rospy.ROSInterruptException:
         pass
