#!/usr/bin/env python
import roslib
import rospy
import time
import csv
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool, Int16, Header, Float32, String

flag = 0

##########################--Data_store_variables---####################################

header_seq_list = []
header_timestamp_secs_list = []
header_timestamp_nsecs_list = []
header_frameid_list = []
orientation_x_list = []
orientation_y_list = []
orientation_z_list = []
orientation_w_list = []
orientation_covariance_list = []
angular_velociy_x_list = []
angular_velociy_y_list = []
angular_velociy_z_list = []
angular_velociy_covariance_list = []
linear_acceleration_x_list = []
linear_acceleration_y_list = []
linear_acceleration_z_list = []
linear_acceleration_covariance_list = []
flag_list = []

######################################################################

def position_node(msg):

    global flag
    flag_list.append(flag)

    header_seq_list.append(msg.header.seq)
    header_timestamp_secs_list.append(msg.header.stamp.secs)
    header_timestamp_nsecs_list.append(msg.header.stamp.nsecs)
    header_frameid_list.append(msg.header.frame_id)

    orientation_x_list.append(msg.orientation.x)
    orientation_y_list.append(msg.orientation.y)
    orientation_z_list.append(msg.orientation.z)
    orientation_w_list.append(msg.orientation.w)
    orientation_covariance_list.append(msg.orientation_covariance)

    angular_velociy_x_list.append(msg.angular_velocity.x)
    angular_velociy_y_list.append(msg.angular_velocity.y)
    angular_velociy_z_list.append(msg.angular_velocity.z)
    angular_velociy_covariance_list.append(msg.angular_velocity_covariance)

    linear_acceleration_x_list.append(msg.linear_acceleration.x)
    linear_acceleration_y_list.append(msg.linear_acceleration.y)
    linear_acceleration_z_list.append(msg.linear_acceleration.z)
    linear_acceleration_covariance_list.append(msg.linear_acceleration_covariance)


######################################################################

def flag_node(data):
    global flag
    flag = data.data
    

######################################################################

if __name__ == "__main__":
    rospy.init_node('imu_node', anonymous=True)
    rospy.Subscriber('/mobile_base/sensors/imu_data', Imu, position_node)
    rospy.Subscriber('/flag_value', Int16, flag_node)
    rospy.spin()

    filehandle = open("data_files/excel_data/robot_imu_data.csv", "w")
    writer = csv.writer(filehandle)
    writer.writerow(["flag_value", "header_seq", "time_stamp_sec", "time_stamp_nsecs", "header_frame_id", "orientation_x", "orientation_y", "orientation_z", "orientation_w","orientation_covariance", "angular_velocity_x", "angular_velocity_y", "angular_velocity_z", "angular_velocity_covariance", "linear_acceleration_x", "linear_acceleration_y", "linear_acceleration_z", "linear_acceleration_covariance"])
    for i in range(len(header_seq_list)):

        a = header_seq_list[i]
        b = header_timestamp_secs_list[i]
        c = header_timestamp_nsecs_list[i]
        d = header_frameid_list[i]
        e = orientation_x_list[i]
        f = orientation_y_list[i]
        g = orientation_z_list[i]
        h = orientation_w_list[i]
        j = orientation_covariance_list[i]
        k = angular_velociy_x_list[i]
        l = angular_velociy_y_list[i]
        m = angular_velociy_z_list[i]
        n = angular_velociy_covariance_list[i]
        o = linear_acceleration_x_list[i]
        p = linear_acceleration_y_list[i]
        q = linear_acceleration_z_list[i]
        r = linear_acceleration_covariance_list[i]
        fg = flag_list[i]

        writer.writerow([fg, a, b, c, d, e, f, g, h, j, k, l, m, n, o, p, q, r])
    filehandle.close()


######################################################################
