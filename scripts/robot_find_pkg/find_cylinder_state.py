#!/usr/bin/python
#coding=utf-8
#Author: Xu

#为状态机模块提供找定位柱的接口
#kinect的坐标系与机器人坐标系不同！

import rospy
from cylinder_detector.srv  import *
import geometry_msgs.msg as g_msgs

class find_cylinder_state(object):
    def __init__(self):
        self.cylinder_client = rospy.ServiceProxy('cylinder_data',cylinderdata)
        self.cmd_vel_pub = rospy.Publisher('cmd_move_robot' , g_msgs.Twist , queue_size=100)
        rospy.loginfo('[cylinder_state_pkg]->waiting cylinderdata service')
        self.cylinder_client.wait_for_service()
        rospy.loginfo('[cylinder_state_pkg] -> connected to cylinder service')


    #边转动边检测定位柱，检测到后停止
    def get_cylinder_status(self):
        self.cylinder_client.wait_for_service()
        res = self.cylinder_client()
        move_velocity = g_msgs.Twist()
<<<<<<< HEAD
<<<<<<< HEAD
        move_velocity.angular.z = -0.13
        x = res.z
        theta = res.theta
        iscylinder = res.has_cylinder
        r = rospy.Rate(50)
        while not rospy.is_shutdown() and not iscylinder:
            self.cmd_vel_pub.publish(move_velocity)
            res = self.cylinder_client()
            x = res.z
=======
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
        move_velocity.angular.z = -0.15
        x = res.x
        theta = res.theta
        iscylinder = res.has_cylinder
        r = rospy.Rate(30)
        while not rospy.is_shutdown() and not iscylinder:
            self.cmd_vel_pub.publish(move_velocity)
            res = self.cylinder_client()
            x = res.x
<<<<<<< HEAD
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
            theta = res.theta
            iscylinder = res.has_cylinder
            if iscylinder == 1:
                self.brake()
                break
            r.sleep()
        return (x,theta)

    #直接获取定位柱的位置信息
    def find_cylinder(self):
        self.cylinder_client.wait_for_service()
        res = self.cylinder_client()
<<<<<<< HEAD
<<<<<<< HEAD
        x = res.z
=======
        x = res.x
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
        x = res.x
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
        theta = res.theta
        return (x,theta)

    def brake(self):
        self.cmd_vel_pub.publish(g_msgs.Twist())


if __name__ == '__main__':
    test = find_cylinder_state()
    print test.get_cylinder_status()
