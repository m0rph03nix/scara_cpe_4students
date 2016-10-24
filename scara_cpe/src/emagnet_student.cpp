#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int16.h"
#include "std_msgs/Bool.h"
#include "serial/serial.h"
#include <string>
#include <sstream>
#include <cstdlib>
#include <ros/callback_queue.h>

void grip_callback(const std_msgs::Bool::ConstPtr& msg);
std::string receive_data(void);
std::string port="/dev/ttyUSB1";

serial::Serial *s;


int main(int argc, char **argv)
{
 unsigned char grip = 0;
 unsigned char detect = 0;
 unsigned char detect_prev = 0;
 //std::string detect = "";
 int baud = 9600; 
 std_msgs::Bool isDetected;

 
 ros::init(argc,argv,"emagnet");
 ros::NodeHandle n;
 

 ros::Publisher detect_metal_pub=n.advertise<std_msgs::Bool>("detect_metal",10);
 ros::Subscriber grip_sub = n.subscribe("grip", 10, grip_callback);

 ros::Rate loop_rate(10);

 serial::Serial serial_arduino(port, baud, serial::Timeout::simpleTimeout(1000));
 s = &serial_arduino;
 
 serial_arduino.setTimeout(serial::Timeout::max(),250,0,250,0);

 ROS_INFO("Serial with arduino is open ?");

 if(serial_arduino.isOpen())
 {
   ROS_INFO("Yes");
 }
 else
 {
   ROS_INFO("No");
 }
 
 s->write(&grip, 1);
 

 while(ros::ok())
 {

      s->read(&detect, 1);
	  
	  // 
	  // To be completed
	  // Publish on detect_metal_pub
	  //

      ros::spinOnce();
      loop_rate.sleep();
 }
 

 return 0;
 

}


void grip_callback(const std_msgs::Bool::ConstPtr& msg)
{
 unsigned char grip = 0;

 if(msg->data) grip = 1;
 else grip = 0;

	
 s->write(&grip, 1);
 ROS_INFO("GRIP : %d",grip);
}


 
