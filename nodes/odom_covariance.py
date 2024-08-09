#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def odom_callback(msg):
    # Set reasonable values for the covariance matrix
    msg.pose.covariance = [
        0.01, 0, 0, 0, 0, 0,
        0, 0.01, 0, 0, 0, 0,
        0, 0, 0.01, 0, 0, 0,
        0, 0, 0, 0.1, 0, 0,
        0, 0, 0, 0, 0.1, 0,
        0, 0, 0, 0, 0, 0.1
    ]
    msg.twist.covariance = [
        0.01, 0, 0, 0, 0, 0,
        0, 0.01, 0, 0, 0, 0,
        0, 0, 0.01, 0, 0, 0,
        0, 0, 0, 0.1, 0, 0,
        0, 0, 0, 0, 0.1, 0,
        0, 0, 0, 0, 0, 0.1
    ]
    odom_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('odom_covariance_corrector')
    odom_sub = rospy.Subscriber('/scanmatch_odom', Odometry, odom_callback)
    odom_pub = rospy.Publisher('/corrected_odom', Odometry, queue_size=10)
    rospy.spin()

