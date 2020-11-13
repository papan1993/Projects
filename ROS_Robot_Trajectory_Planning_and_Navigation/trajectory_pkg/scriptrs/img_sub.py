#!/usr/bin/env python
import roslib
import sys
import rospy
import cv
import time
import cv2
import csv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Bool, Int16, Header, Float32, String

#flag = 0
#flag2 = 1
num = 0
time_now = 0
time_list = []
num_list = []

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)
    #self.image_sub = rospy.Subscriber('/flag_value', Int16, self.flag_node)

  def callback(self,data):
    try:
        global num
        global time_now
        # global flag
        # global flag2
        cv_image = self.bridge.imgmsg_to_cv2(data, "rgb8")
        time_str = time.time()
        time_later = time.time()
        diff = (time_later - time_now)
        diff = round(diff, 1)

        if (diff == 0.2):
            time_list.append(time_str)
            num_list.append(num)
            cv2.imwrite("data_files/images/frame_" + str(num) + ".png", cv_image)
            print("---- image saved ---Number---", str(num))
            num = num + 1
            time_now = time_later

        # if (num == 0):
        #     cv2.imwrite("images/frame_"+str(num)+".png", cv_image)
        #     print("---- image saved ---Number---", str(num))
        #     num = num + 1
        #
        # if (flag2 == flag):
        #     cv2.imwrite("images/frame_"+str(flag2)+".png", cv_image)
        #     print("---- image saved ---Number---", str(flag2))
        #     flag2 =  flag2 + 1

    except CvBridgeError, e:
        print("--error---", e)

#################################################################################

  # def flag_node(self,data):
  #     global flag
  #     flag = data.data

#################################################################################

def main_func():
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
      global time_now
      time_now = time.time()
      rospy.spin()
  except KeyboardInterrupt:
      print("-----shutting down---")

  filehandle = open("data_files/excel_data/images_time_stamp_data.csv", "w")
  writer = csv.writer(filehandle)
  writer.writerow(["image_number", "time_stamp"])
  for i in range(len(num_list)):
      x = num_list[i]
      y = time_list[i]
      writer.writerow([x, y])
  filehandle.close()

if __name__ == '__main__':
    main_func()
