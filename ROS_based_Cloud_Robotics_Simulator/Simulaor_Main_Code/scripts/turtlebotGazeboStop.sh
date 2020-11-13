#!/bin/bash
pkill -f xterm
pkill -f spawner

#====Deleting Model Files====

rm -rf ~/.gazebo/models/finalEnv
rm -rf ~/.gazebo/models/groundPlaneWithChessBoardPattern
