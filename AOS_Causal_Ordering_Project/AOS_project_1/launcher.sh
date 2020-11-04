#!/bin/bash

#### Change this to your netid
netid=sxc180056

#### Root directory of your project
PROJDIR=/home/013/s/sx/sxc180056/AOS_Projects/AOS_project_1

#### Directory where the config file is located on DC system
CONFIGDC=$PROJDIR/Config_dc_test_3.dat

#### Config File local machine
CONFIGLOCAL=/home/soumyadeep/IdeaProjects/AOS_project_1/Config_dc_test_3.dat

# Directory your java classes are in
BINDIR=$PROJDIR/src

# Your main project class
PROG=Main

n=0

cat $CONFIGLOCAL | sed -e "s/#.*//" | sed -e "/^\s*$/d" |
(
  read i
  echo "Number of Nodes - " $i
  while [[ $n -lt $i ]]
  do
    read line
    p=$( echo $line | awk '{ print $1 }' )
    echo $p
    host=$( echo $line | awk '{ print $2 }' )
    echo $host
	  gnome-terminal -e "bash -c 'ssh -o StrictHostKeyChecking=no $netid@$host java -cp $BINDIR $PROG $CONFIGDC $p;$SHELL'" &
	  n=$(( n + 1 ))
  done
)
