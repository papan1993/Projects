#!/bin/bash

#####################----Launch-codes----####################

#cd /home/soumyadeep/traj_research/
#xterm -iconic -e roslaunch exp_world.launch

################################################################

xterm -iconic -e roscore &
sleep 2

################################################################

xterm -iconic -e roslaunch turtlebot_bringup minimal.launch &
sleep 5
xterm -iconic -e roslaunch freenect_launch freenect.launch &
sleep 5
#xterm -iconic -e rosrun rqt_image_view rqt_image_view &
#sleep 4

################################################################

cd ~/traj_ws/src/trajectory_pkg/scripts/
#xterm -iconic -e python ./imu_sub_traj.py &
xterm -iconic -e python ./imu_sub_teleop.py &
sleep 5

################################################################

cd ~/traj_ws/src/trajectory_pkg/scripts/
#xterm -iconic -e python ./odom_sub_traj.py &
xterm -iconic -e python ./odom_sub_teleop.py &
sleep 5

################################################################

#cd ~/traj_ws/src/trajectory_pkg/scripts/
#xterm -iconic -e python ./img_sub.py &
#sleep 2

################################################################

cd ~/traj_ws/src/trajectory_pkg/scripts/
xterm -iconic -e python ./rec_vid.py &
sleep 2

################################################################

#cd ~/traj_ws/src/trajectory_pkg/scripts/
#xterm -iconic -e python ./pub_twist_multi.py

################################################################
