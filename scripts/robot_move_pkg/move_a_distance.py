#!/usr/bin/env python
#coding:utf-8
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
# author = hao , rescuer liao
#send a distance to move

#append the robot state pkg to the python path

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592

#Team unware basketball robot nwpu
#在X或Y轴上设置一段距离，机器人移动相应的距离

# author = liao-zhihan , hao

#first_debug_date = 2015-07
#first_debug: 第一次测试通过

#second_debug_date = 2016-03-02 author=liao-zhihan
#second_debug:重写代码，对代码进行了规范

#################################################
#注意添加坐标获取模块路径到pth!                 #
#################################################

import math
import rospy
import config
import sys
sys.path.append(config.robot_state_pkg_path)#请修改配置文件中地址
import robot_state_pkg.get_robot_position as robot_state
import geometry_msgs.msg as g_msgs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import interpolation_function.growth_curve as sp_func
=======

>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======

>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
import interpolation_function.growth_curve as sp_func
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
import interpolation_function.growth_curve as sp_func
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
class move_a_distance(object):
    def __init__(self):
        rospy.loginfo('[robot_move_pkg]->move_a_distance is initial')
        self.robot_state = robot_state.robot_position_state()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self.stop_tolerance = config.high_speed_stop_tolerance
        self.cmd_move_pub = rospy.Publisher('/cmd_move',g_msgs.Twist , queue_size=100)
        self.vel_sp = sp_func.growth_curve()
=======
        self.speed = config.linear_move_speed
        self.stop_tolerance = config.linear_move_stop_tolerance
        self.cmd_move_pub = rospy.Publisher('/cmd_move',g_msgs.Twist , queue_size=100)
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
        self.speed = config.linear_move_speed
        self.stop_tolerance = config.linear_move_stop_tolerance
        self.cmd_move_pub = rospy.Publisher('/cmd_move',g_msgs.Twist , queue_size=100)
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
        self.stop_tolerance = config.high_speed_stop_tolerance
        self.cmd_move_pub = rospy.Publisher('/cmd_move',g_msgs.Twist , queue_size=100)
        self.vel_sp = sp_func.growth_curve()
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
        self.stop_tolerance = config.high_speed_stop_tolerance
        self.cmd_move_pub = rospy.Publisher('/cmd_move',g_msgs.Twist , queue_size=100)
        self.vel_sp = sp_func.growth_curve()
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592

    #发送即停速度，机器人停止
    def brake(self):
        move_velocity = g_msgs.Twist()
        move_velocity.linear.x = 0.0
        move_velocity.linear.y = 0.0
        self.cmd_move_pub.publish(move_velocity)

    #在X或者Y轴移动一段距离，注意只可在一个轴上移动！
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def move_to(self , x = 0.0 , y = 0.0):
=======
    def move_to(self , x = 0 , y = 0):
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
    def move_to(self , x = 0 , y = 0):
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
    def move_to(self , x = 0.0 , y = 0.0):
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
    def move_to(self , x = 0.0 , y = 0.0):
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
        try:
            if x!=0 and y!=0:
                raise Exception('[robot_move_pkg]->move_a_distance can not send the '
                                'distance x and y at the same time, use move_to_point instead!')
        except Exception,e:
            print e

        if x==0:
            rospy.loginfo('[robot_move_pkg]->move_a_distance will move to y = %s'%y)
            self.start_move(y = y)
        else:
            rospy.loginfo('[robot_move_pkg]->move_a_distance will move to x = %s'%x)
            self.start_move(x = x)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
    #开始移动
    def start_move(self,x = 0.0 , y = 0.0):
        rospy.on_shutdown(self.brake) #当系统停止时，机器人也停止
        r = rospy.Rate(100)
        move_on_x = (y==0)
        if move_on_x:
            self.vel_sp.set_goal_distance(abs(x))
        else:
            self.vel_sp.set_goal_distance(abs(y))
    ############获得机器人当前的位置作为起始位置##################
        start_x,start_y = self.robot_state.get_robot_current_x_y()  
        current_x , current_y = start_x , start_y
        move_velocity = g_msgs.Twist()
        is_arrive_goal = False
        # 如果系统没有停止，且还没有到达终点
        while not rospy.is_shutdown() and is_arrive_goal is not True:
            if not is_arrive_goal:
                # 获取当前的位置
                current_x,current_y = self.robot_state.get_robot_current_x_y()
                # 计算距离终点的欧式距离
                distance_has_moved =  math.sqrt(pow(current_x - start_x,2) + pow(current_y - start_y,2))
                if move_on_x:
                    # 计算出还应行走的距离
                    distance_to_arrive_goal_x = abs(x) - distance_has_moved
                    # 如果已经到达了目标的误差范围内
                    if abs(distance_to_arrive_goal_x) <= self.stop_tolerance:
                        is_arrive_goal = True
                        break
                    self.speed = self.vel_sp.cal(distance_has_moved)
        ################计算出速度方向###################
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153

	#开始移动
    def start_move(self,x = 0 , y = 0):
        rospy.on_shutdown(self.brake) #当系统停止时，机器人也停止
        r = rospy.Rate(100)
        move_on_x = (y==0)

	############获得机器人当前的位置作为起始位置##################
        start_x,start_y = self.robot_state.get_robot_x_y()  
        current_x , current_y = start_x , start_y

        move_velocity = g_msgs.Twist()
        is_arrive_goal = False
        while not rospy.is_shutdown() and is_arrive_goal is not True:#如果系统没有停止，且还没有到达终点
            if not is_arrive_goal:
                current_x,current_y = self.robot_state.get_robot_x_y()#获取当前的位置
                distance_has_moved =  math.sqrt(pow(current_x - start_x,2) + pow(current_y - start_y,2))#计算距离终点的欧式距离

                if move_on_x:
                    distance_to_arrive_goal_x = abs(x) - distance_has_moved #计算出还应行走的距离
                    if abs(distance_to_arrive_goal_x) <= self.stop_tolerance: #如果已经到达了目标的误差范围内
                        is_arrive_goal = True
                        break

			#################计算出速度方向###################
<<<<<<< HEAD
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
                    if x > 0:
                        move_velocity.linear.x = math.copysign(self.speed , distance_to_arrive_goal_x)
                    else:
                        move_velocity.linear.x = math.copysign(self.speed, -distance_to_arrive_goal_x)
                    move_velocity.linear.y = 0.0
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    self.cmd_move_pub.publish(move_velocity)
=======
                    self.cmd_move_pub.publish(move_velocity)#根据配置文件的设置速度，使机器人移动
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
                    self.cmd_move_pub.publish(move_velocity)#根据配置文件的设置速度，使机器人移动
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
                    self.cmd_move_pub.publish(move_velocity)
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
                    self.cmd_move_pub.publish(move_velocity)
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592

                else :
                    distance_to_arrive_goal_y = abs(y) - distance_has_moved
                    if distance_to_arrive_goal_y <= self.stop_tolerance:
                        is_arrive_goal = True
                        break
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    self.speed = self.vel_sp.cal(distance_has_moved)
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
                    self.speed = self.vel_sp.cal(distance_has_moved)
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
                    self.speed = self.vel_sp.cal(distance_has_moved)
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
                    move_velocity.linear.x = 0.0
                    if y > 0:
                        move_velocity.linear.y = math.copysign(self.speed , distance_to_arrive_goal_y)
                    else:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
                        move_velocity.linear.y = math.copysign(self.speed ,-distance_to_arrive_goal_y)
                self.cmd_move_pub.publish(move_velocity)
            r.sleep()
        self.brake()#目标距离以达到，停止移动

if __name__ == '__main__':
    rospy.init_node('move_cmd')
    move_cmd = move_a_distance()
#    move_cmd.move_to(x = 1.2)
    move_cmd.move_to(y = 6.0)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
                        move_velocity.linear.y = math.copysign(self.speed, -distance_to_arrive_goal_y)
                    self.cmd_move_pub.publish(move_velocity)

            r.sleep()
        self.brake()#目标距离以达到，停止移动



if __name__ == '__main__':
    rospy.init_node('move_cmd')
    move_cmd = move_a_distance()
    move_cmd.move_to(x = 0.8)
<<<<<<< HEAD
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
    sys.path.remove(config.robot_state_pkg_path)
