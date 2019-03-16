# Pack name here

## Overview

This is a [ROS] package developed for ... with a mobile robot. 

This package has been tested under ROS Kinetic and Ubuntu 16.04. This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

**Author: Markus Lamprecht<br />
Maintainer: Markus Lamprecht, 2f4yor@gmail.com<br />**

<img alt="alfons" src="data/alfons.png" width="700">

## Installation

### Dependencies

This software is built on the Robotic Operating System ([ROS]), which needs to be [installed](http://wiki.ros.org) first. Additionally, this package depends on following software:

- [Eigen](http://eigen.tuxfamily.org) (linear algebra library).


### Building

In order to install this package, clone the latest version from this repository into your catkin workspace and compile the package using [catkin_tools](https://catkin-tools.readthedocs.io/en/latest/)

    cd catkin_workspace/src
    git clone git@github.com:CesMak/alfons_robot_bringup.git
    cd ..
    catkin init
    catkin build


## Basic Usage

## Main Launch file

``` 

``` 

## Nodes

### Node: name1

description

#### Subscribed Topics

* **`/points`** ([sensor_msgs/PointCloud2])

    The distance measurements.


#### Published Topics

* **`name`** ([grid_map_msg/GridMap])

     description


#### Services

* **`trigger_fusion`** ([std_srvs/Empty])

    Trigger the fusing process for the entire elevation map and publish it. For example, you can trigger the map fusion step from the console with

        rosservice call /elevation_mapping/trigger_fusion

#### Parameters

* **`point_cloud_topic`** (string, default: "/points")

    The name of the distance measurements topic.


## License BSD
If you want to use this package please contact: [me](https://simact.de/about_me).

## Bugs & Feature Requests

Please report bugs and request features using the Issue Tracker


## TODO's



[ROS]: http://www.ros.org
[rviz]: http://wiki.ros.org/rviz
[grid_map_msg/GridMap]: https://github.com/anybotics/grid_map/blob/master/grid_map_msg/msg/GridMap.msg
[sensor_msgs/PointCloud2]: http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html
[geometry_msgs/PoseWithCovarianceStamped]: http://docs.ros.org/api/geometry_msgs/html/msg/PoseWithCovarianceStamped.html
[tf/tfMessage]: http://docs.ros.org/kinetic/api/tf/html/msg/tfMessage.html
[std_srvs/Empty]: http://docs.ros.org/api/std_srvs/html/srv/Empty.html
[grid_map_msg/GetGridMap]: https://github.com/anybotics/grid_map/blob/master/grid_map_msg/srv/GetGridMap.srv
[grid_map_msgs/ProcessFile]: https://github.com/ANYbotics/grid_map/blob/master/grid_map_msgs/srv/ProcessFile.srv

