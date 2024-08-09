#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from message_filters import ApproximateTimeSynchronizer, Subscriber

def callback(odom, imu):
    # Process synchronized messages here
    # rospy.loginfo("Synchronized messages received")
    pass

def sync_node():
    rospy.init_node('sync_node')

    odom_sub = Subscriber('/corrected_odom', Odometry)
    imu_sub = Subscriber('/imu/data_filtered', Imu)

    ats = ApproximateTimeSynchronizer([odom_sub, imu_sub], queue_size=10, slop=0.1)
    ats.registerCallback(callback)

    rospy.spin()

if __name__ == '__main__':
    sync_node()

