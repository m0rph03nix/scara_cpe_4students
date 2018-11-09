
# scara_cpe

## Description
Scara_cpe is a little robot arm designed by Raphael Leber. This robot had been created for educationnal purposes. It is used in practical work in the engineering school CPE LYON, France.

The packages are described as follows :
- scara_cpe_description :
  - Robot urdf (xacro) with mesh files and gazebo tags
  - A launch file allows a visualization of the arm with Rviz with a GUI to move it
- scara_cpe_robot :
  - Specific files for the "real" robot (e.g. dynamixel controllers)
- scara_cpe_gazebo : 
  - Specific files for the gazebo simulation
- scara_cpe_ik_moveit_plugin :
  - IK-Fast generated (and customized) MoveIt! plugin for the scara_cpe robot

![scara_cpe_photo](https://github.com/m0rph03nix/scara_cpe_4students/blob/master/img/scara_cpe_photo.jpg)

### Material description
The scara_cpe is a robot arm is a simplified version of a scara industrial robot. 
The robot is made of :
- 2 dynamixel motors AX-12A
- 4 printed PLA parts
- 1 steel bracket (to hold the robot with a computer case)
- 1 electromagnet, to detect and grab coins (tested with euros coins of 1, 2 and 5 cents)
- 1 electronic board to drive an electromagnet as an actuator and as a inductive sensor. 


### Set up configuration
- This project had been tested under ROS indigo
- Git clone this project in the src of a catkin workspace (e.g. catkin_move/src) and source it in your bashrc
- In order to use Gazebo properly (french install only), in your bashrc add  ``` export LC_NUMERIC=C ``` 
- Add a symbolic link (or a copy) of the "kinect_ros" folder (from scara_cpe_gazebo/models) in ~/.gazebo/models/


## CPE Pratical work instructions (goal, steps and evaluation)

The practical work has to be done in pairs or alone. It will be 20 hours long and splited into 4 main parts, with throughout a same goal : <b>Learn to move a robot arm with ROS</b>
A report and the code (commented) must be deposited on CPE e-Campus before the examination. The report should answer the following questions and should not contain code. However, you can refer to the project files and put screenshots if relevant !
This practical work counts for 1/3 of the final grade
The examination will be a 4 hours individual practical work. It counts for 2/3 of the final grade. Your evaluated skills will start from URDF design to collision avoidance with MoveIt!

## PART 1 - Tools and techno introduction
[Link to the PART1](https://github.com/m0rph03nix/scara_cpe_4students/wiki/PART-1---Tools-and-techno-introduction)

