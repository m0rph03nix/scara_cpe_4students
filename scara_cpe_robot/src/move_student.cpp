#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "state_publisher");
    ros::NodeHandle n;
    ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
    ros::Rate loop_rate(30);

    const double degree = M_PI/180;

    // robot state
    double joint_1 = 0.0F;
	double joint_2 = 0.0F;

    // message declarations
    sensor_msgs::JointState joint_state;


    while (ros::ok()) {
        //update joint_state
        joint_state.header.stamp = ros::Time::now();
        joint_state.name.resize(2);
        joint_state.position.resize(2);
        joint_state.name[0] = // To be completed
		joint_state.position[0] = // To be completed
		// 
		// To be completed
		// 

		joint_pub.publish(joint_state);


        // Create new robot state
        joint_1 += 0.01;
		joint_2 += 0.01;

        // This will adjust as needed per iteration
        loop_rate.sleep();
    }

    return 0;
}
