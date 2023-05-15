#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def clover_goal():
    rospy.init_node('recodrone_goal')
    goal_pub = rospy.Publisher('/goal', PoseStamped, queue_size=10,)
    pose_msg =  PoseStamped()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        goal_pub.publish(pose_msg)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        clover_goal()
    except rospy.ROSInterruptException:
        pass
