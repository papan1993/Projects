#!/bin/bash

#===============Robots Start Position===============

ArrayForY=(0 5.85 5.85 -5.84)
ArrayForZ=(0 5.85 -5.84 -5.84)

#===============Copying Model Files=================

cp -r ../gazeboModelsAndWorldFile/finalEnv ~/.gazebo/models
cp -r ../gazeboModelsAndWorldFile/groundPlaneWithChessBoardPattern ~/.gazebo/models
sleep 2

#===================================================

count=1
NumberOfRobots=4
xterm -iconic -e roslaunch cloud_robotics_simulator my_room_gazebo.launch &
sleep 5
while [ $count -le $(($NumberOfRobots-1)) ]
do
        x='Robot'
        y=$count
        z=$x$y
        echo $z
        echo ${ArrayForY[$count]}
        echo ${ArrayForZ[$count]}
	xterm -iconic -e roslaunch cloud_robotics_simulator robots.launch robot_prefix:=$z x:=${ArrayForY[$count]} y:=${ArrayForZ[$count]} Y:=0.1 &
        xterm -iconic -e roslaunch cloud_robotics_simulator turtlebot_active.launch robot_prefix:=$z initial_pose_x:=${ArrayForY[$count]} initial_pose_y:=${ArrayForZ[$count]} initial_pose_a:=0.1 &
((count++))
done
