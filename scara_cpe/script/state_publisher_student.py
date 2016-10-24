#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState as JointStateMoveIt
from dynamixel_msgs.msg import JointState as JointStateDynamixel
from std_msgs.msg import Int16

SHOULDER_1_INDEX = 0
SHOULDER_2_INDEX = 1

class JointStatePublisher():

    def __init__(self):
        rospy.init_node('state_publisher')

        rate = 15 # Hz
        r = rospy.Rate(rate)


        self.name = ['','']
        self.current_pos = [0.0, 0.0]
        self.velocity = [0.0, 0.0]
        self.load = [0.0, 0.0]        


        # Start controller state subscribers
        rospy.Subscriber('/shoulder_1_controller/state', JointStateDynamixel, self.shoulder1_state_handler)
        rospy.Subscriber('/shoulder_2_controller/state', JointStateDynamixel, self.shoulder2_state_handler)
	
        # Start publisher
        self.joint_states_pub = rospy.Publisher('/joint_states', JointStateMoveIt, queue_size=10)

        while self.name[0]=='' or self.name[1]=='' :
            r.sleep()

        #r.sleep()

        rospy.loginfo("Publishing joint_state at " + str(rate) + "Hz")

        while not rospy.is_shutdown():
            self.publish_joint_states()
            r.sleep()

    def shoulder1_state_handler(self, msg):

        self.name[SHOULDER_1_INDEX] 		= msg.name
        #
        # To be completed ...
        #

    def shoulder2_state_handler(self, msg):

        #
        # To be completed ...
        #



    def publish_joint_states(self):
        # Construct message & publish joint states
        #
        # To be completed ...
        #


if __name__ == '__main__':
    try:
        JointStatePublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
