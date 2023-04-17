# Information: https://clover.coex.tech/programming

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

navigate = rospy.ServiceProxy('navigate', srv.Navigate)

print('Take off and hover 1 m above the ground')
navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)

# Wait for 5 seconds
rospy.sleep(5)

