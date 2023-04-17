#! /usr/bin/env python 

import rospy
from clover import srv
from std_srvs.srv import Trigger
from geometry_msgs.msg import Twist

rospy.init_node('flight')

navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
land = rospy.ServiceProxy('land', Trigger)

def velocity(data):
    nz = data.linear.z
    nx = data.linear.x
    ny = data.linear.y
    yr = data.angular.z
    #print("Moving forward at %f m/s and rotating at %f rad/s" % round(nx, 5) % round(yr, 5))
    set_velocity(vx=nx, vy=ny, vz=nz, yaw=float('nan'),yaw_rate=yr, frame_id='body')


rospy.Subscriber("cmd_vel", Twist, velocity)

rospy.spin()
