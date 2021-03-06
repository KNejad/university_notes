#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def twister():
  rospy.init_node('twister', anonymous=True)
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  rate = rospy.Rate(5) # 5hz
  while not rospy.is_shutdown():
    tw=Twist()
    tw.linear.x=1 #move forward
    tw.angular.z=1 #and turn left
    pub.publish(tw)
    rate.sleep()

if __name__ == '__main__':
    try:
        twister()
    except rospy.ROSInterruptException:
        pass
