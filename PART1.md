## PART 1 - Tools and techno introduction

### 1.1 URDF comes to life !
- In the package ``` scara_cpe_description ```  launch ``` scara_cpe_gui.launch ```
	- Move the arm with the GUI (user interface, here with 2 sliders to move the 2 joints)
	 - Analyse the launch file :
		 - Which nodes are launched ? 
		 - Which node loads the urdf file ? 
		 - Which node run the GUI ?
		 - What is xacro ? Check how it's used in the urdf file ```scara_cpe_description/urdf/scara_cpe.xacro```
	 - Check the URDF (xacro) file(s) :
		 - What's the joints name ?
		 - What's the exact distance between base_link and the effector when the arm is straight ?

### 1.2 GAZEBO simulation and Rviz vizualisation
- Kill previous nodes
- What is Gazebo ? What is Rviz ? In what are they completly different tools ?
- In the package ``` scara_cpe_gazebo ```  launch ``` gazebo_scara_playground.launch ```
	- Gazebo is a bit "sensitive"... try once again if it fails (and try once more...)
	- Look in the world file, and write down the (X,Y) coordinates of the colored cylinders 
	- List the availables topics and try to "see" in Rviz as much as you can get from them. 
	- Save the rviz workspace you just prepared in ``` scara_cpe_gazebo/config/sim.rviz ```
	- In ``` scara_cpe_gazebo/launch ``` create ``` scara_gazebo_rviz.launch ```:
		- include ``` gazebo_scara_playground.launch ```
		- call Rviz with the rviz file you just created

### 1.3 ROS Actions and controllers
- Read [the wiki page of actionlib](http://wiki.ros.org/actionlib) and sum up in a few lines what is a ROS action
- List the availables topics and identify a ROS Action. 
- Write an action client in python to send 1,5 rad to each joint. Consider the following instructions :
	- Package (new) : ```scara_cpe_kinematics``` 
	- Emplacement (new) : ```scara_cpe_kinematics/script``` 
	- Name of the file : ``` gazebo_trajectory_action_client_test.py``` 
	- Check that the robot moves well in Gazebo

### 1.4 Kinematics
- Still in ```scara_cpe_kinematics/script``` , create the file ```ik_service_action_client.py```:
	- Copy/paste your code from ``` gazebo_trajectory_action_client_test.py``` 
	- Add in your code the invert kinematics algorithme you calculated in the preparation of the practical work of "Modélisation des robots". So from (X, Y) in inputs, calculate 
![Theta1, Theta2](http://latex.codecogs.com/gif.download?%28%5CTheta_1%2C%20%5CTheta_2%29)
	- Test first your code by sending sequentially the (X, Y) coordinates of the red disk and the yellow disk.
	- Create a service which call in its callback the inverse kinematics function and the action of the trajectory controller :
		- Name of the service : gotoxy
		- Goal of the service : Move the effector to the coordinates (X, Y)
		- Name of the srv file: GoToXY
		- Request : "x" and "y" as floating numbers --> Coordinates to reach
		- Response : "finised" as a boolean --> Return True when the mouvement is over
		- Name of the service callback function : gotoxy
	- Call the service from a terminal
	- Options if you still have some time : 
		- Optimise the trajectory duration thanks to the difference with the previous angles, the max speed and the max acceleration. The duration to keep is the worst (longest) of the 2 joints.
		- Optimise the selection of the option "top elbow" and "down elbow" by keeping the one with shortest angles (delta) to reach.
-  In ```scara_cpe_kinematics/launch``` , create  ```ik_gazebo.launch``` :
	- Include ``` gazebo_scara_playground.launch ```
	- Call ``` gazebo_trajectory_action_client_test.py``` 


