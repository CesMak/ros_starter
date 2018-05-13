#!/bin/bash

description_name=$1

if [ "$description_name" == "" ]
    then
        description_name="example"
fi

echo "git, catkin, ros>=indigo required"
echo "Please enter the name of your new model_description:"
mkdir -p /tmp/my_catkin_ws/src
cd /tmp/my_catkin_ws/src
git clone git@github.com:CesMak/ros_starter.git .
python create_gz_model.py "$description_name"

cd /tmp/my_catkin_ws
catkin init
catkin build
source /tmp/my_catkin_ws/devel/setup.bash
. /tmp/my_catkin_ws/devel/setup.bash
#roscd "$description_name"+"_description"
