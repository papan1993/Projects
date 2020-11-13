#!/bin/bash

#========DISTINCT_RANDOM_2D_NUMBER_GENERATOR========

i=0
y=0
a=0
flag=0
temp=0
MaximumCount=12 #No. of grids (lies between -8 to +8)
NoOfGrid=$(expr $MaximumCount + 1)
MaxRobots=$(expr $NoOfGrid \* $NoOfGrid)
read -p "Number of Robots (1 - $MaxRobots ) : " NumberOfRobots
while [ $NumberOfRobots -lt 1 ] || [ $NumberOfRobots -gt $MaxRobots ]
do
clear
echo -en '\E[47;31m'"\033[1mErrr...ERROR. Number out of range. Please Enter Again.\033[0m"
echo; echo
read -p "Number of Robots (1 - $MaxRobots ) : " NumberOfRobots
done
ArrayForX=()
ArrayForY=()
ArrayForZ=()
ArrayToCompare=()
flag=$(expr $MaximumCount / 2) 
while [ $i -le $MaximumCount ]
do
if [ $i -lt $flag ]
then
ArrayForX[$i]=-$(expr $flag - $i)
else
ArrayForX[$i]=$(expr $i - $flag)
fi
((i++))
done
echo "${ArrayForX[@]}"
MultiplierX=$(( ( RANDOM % $MaximumCount )  + 1 ))
MultiplierY=$(( ( RANDOM % $MaximumCount )  + 1 ))
temp=${ArrayForX[$MultiplierX]}${ArrayForX[$MultiplierY]}
ArrayToCompare[$a]=$temp
ArrayForY[$a]=${ArrayForX[$MultiplierX]}
ArrayForZ[$a]=${ArrayForX[$MultiplierY]}
while [ $a -lt $(($NumberOfRobots-1)) ]
do
MultiplierX=$(( ( RANDOM % $MaximumCount )  + 1 ))
MultiplierY=$(( ( RANDOM % $MaximumCount )  + 1 ))
temp=${ArrayForX[$MultiplierX]}${ArrayForX[$MultiplierY]}
flag=0
while [ $y -le $a ]
do
if [ ArrayToCompare[$y] == $temp ]
then
flag=1
break
fi
((y++))
done
if [ $flag -eq 0 ]
then
((a++))
ArrayToCompare[$a]=$temp
ArrayForY[$a]=${ArrayForX[$MultiplierX]}
ArrayForZ[$a]=${ArrayForX[$MultiplierY]}
fi
done

#===================================================

count=0
robotsCount=0
xterm -iconic -e roslaunch ~/simulation_project/launchFilesForMultipleRobots/my_room_gazebo.launch &
sleep 10
while [ $count -le $(($NumberOfRobots-1)) ]
do
        x='Robot'
        y=$count
        z=$x$y
        echo $z
        echo ${ArrayForY[$count]}
        echo ${ArrayForZ[$count]}
	xterm -iconic -e roslaunch ~/simulation_project/launchFilesForMultipleRobots/robots.launch robot_prefix:=$z x:=${ArrayForY[$count]} y:=${ArrayForZ[$count]} Y:=0.1 &
        ((count++))
done
