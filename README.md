## Call it via:
Simply download the .sh file and call it:
./easy_start_ros.sh marble


## Then do:
roscd marble_description

## Launch and start it in rviz:
roslaunch marble_description marble_description.launch

## The easy_start_ros.bash script does the following:
	description_name=$1
	echo "git, catkin, ros>=indigo required"
	echo "Please enter the name of your new model_description:"
	mkdir -p /tmp/my_catkin_ws/src
	cd /tmp/my_catkin_ws/src
	git clone git@github.com:CesMak/ros_starter.git .
	python create_gz_model.py "$description_name"
	cd /tmp/my_catkin_ws
	catkin init
	catkin build
	cd /tmp/my_catkin_ws/devel
	source /tmp/my_catkin_ws/devel/setup.bash

