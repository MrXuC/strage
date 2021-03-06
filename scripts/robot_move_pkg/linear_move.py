#!/usr/bin/env python
#coding:utf-8

#Team unware basketball robot nwpu
#在X和Y轴上设置一段距离，同时设置一定的角度值，机器人移动相应的距离以及转相应角度


# 2016-7-18
# 将直线移动速度和角速度进行了关联
import rospy
import geometry_msgs.msg as g_msgs
import  math
import config
import  sys
sys.path.append(config.robot_state_pkg_path)
import robot_state_pkg.get_robot_position as robot_state#注意修改路径
import turn_an_angular
import interpolation_function.growth_curve as spline_func

class linear_move(object):
    def __init__(self):
        rospy.loginfo('[robot_move_pkg]->linear_move is initial')
        #通过这个模块获取机器人当前姿态
        self.robot_state = robot_state.robot_position_state()
        self.cmd_move_pub = rospy.Publisher('/cmd_move', g_msgs.Twist, queue_size = 100)
        self.rate = rospy.Rate(100)
        #设置机器人直线移动阈值
        self.stop_tolerance = config.high_speed_stop_tolerance
        self.angular_tolerance = config.high_turn_angular_stop_tolerance
        #通过这个模块修正最终姿态角
        self.accurate_turn_an_angular = turn_an_angular.turn_an_angular()
        self.x_speed = 0.0
        self.y_speed = 0.0
        self.w_speed = config.high_turn_angular_speed
        #进行线速度插值
        self.linear_sp = spline_func.growth_curve()

<<<<<<< HEAD
<<<<<<< HEAD

=======
        
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
        
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
    def brake(self):#停止时的回调函数
        rospy.loginfo('The robot is stopping...')
        move_velocity = g_msgs.Twist()
        move_velocity.linear.x = 0
        move_velocity.linear.y = 0
        move_velocity.angular.z = 0
        self.cmd_move_pub.publish(move_velocity)


    def start_run(self,x = 0.0, y = 0.0, yaw = 0.0):#开始移动
        #设置停止回调函数
        rospy.on_shutdown(self.brake)
        move_velocity = g_msgs.Twist()
        # 计算目标移动欧拉距离
        goal_distance = math.sqrt(math.pow(x, 2)+math.pow(y, 2))
        # 算出方向角,便于接下来的分解
        direction_angle = math.atan2(y , x)
        # 获取启动前的x，y，yaw
        start_x, start_y, start_yaw = self.robot_state.get_robot_current_x_y_w()
        # 设置目标插值距离，确定最终插值曲线
        self.linear_sp.set_goal_distance(abs(goal_distance))
        self.is_arrive_goal = False
        angular_has_moved = 0.0
        # 构建goal_angular 和 goal_distance 的函数关系后等式两边对dt取微分可得
        # w = df(goal_distance)/dgoal_distance * v
        # 因为我们简单的将goal_angular 和 goal_distance 构建为线性关系,所以最终角速度和线速度的关系为
        # w = goal_angular/goal_distance * v
        # 在这里,因为线速度不是完美连续的,所以为了让角度移动和直线移动尽量保持同步,所以加上了一个系数0.02
        # 0.02只是目前的一个补偿系数,可以进行大量的调试来精准的确定
        cov_func =lambda x: x*abs(yaw)/ goal_distance +0.02
        while not rospy.is_shutdown() and goal_distance != 0:
            if self.is_arrive_goal == False:
                current_x , current_y, current_yaw = self.robot_state.get_robot_current_x_y_w()
                distance_has_moved = math.sqrt( math.pow(current_x - start_x, 2)+
                                                math.pow(current_y - start_y, 2))
                # 此速度是插值算出的线速度
                linear_speed = self.linear_sp.cal(distance_has_moved)
                #  算出走了多少弧度
                angular_has_moved += abs(abs(current_yaw) - abs(start_yaw))
                start_yaw  = current_yaw
                # 角度在阈值之外就计算角速度,反之赋零
                if yaw != 0.0 and abs(angular_has_moved - abs(yaw)) > self.angular_tolerance:
                    move_velocity.angular.z = math.copysign(cov_func(linear_speed), yaw)
                else:
                    move_velocity.angular.z = 0.0
                # 将插值算出来的速度进行分解
                self.x_speed = linear_speed * math.cos(direction_angle)
                self.y_speed = linear_speed * math.sin(direction_angle)
                # 这个直线移动距离是为了与接下来的阈值比较
                distance_to_arrive_goal = distance_has_moved - goal_distance
                move_velocity.linear.x = math.copysign(self.x_speed, x)
                move_velocity.linear.y = math.copysign(self.y_speed, y)
                if abs(distance_to_arrive_goal) <= self.stop_tolerance:
                    self.is_arrive_goal = True
                    break
            self.cmd_move_pub.publish(move_velocity)
            self.rate.sleep()
        self.brake()
        print angular_has_moved
#        修正角度转动偏差，同时如果x，y均为零时转动角度
#        self.accurate_turn_an_angular.turn(self.normalize_angle(yaw - current_yaw + start_yaw))

    def move_to(self, x= 0.0, y= 0.0, yaw= 0.0):
<<<<<<< HEAD
<<<<<<< HEAD
     #'''提供给外部的接口,移动某一距离、角度'''
=======
    # 提供给外部的接口
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
    # 提供给外部的接口
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
        rospy.loginfo('[robot_move_pkg]->linear_move will move to x_distance = %s y_distance = %s, angular = %s'%(x,y,yaw))
        if x == 0.0 and y == 0:
            self.accurate_turn_an_angular.turn(self.normalize_angle(yaw))
        else:
            self.start_run(x, y, yaw)
<<<<<<< HEAD
<<<<<<< HEAD
            
    def move_to_pose(self, x = 0.0, y = 0.0, yaw = 0.0):
        '''提供给外部的接口，移动到某一姿态'''
        rospy.loginfo('[robot_move_pkg]->linear_move will move to x_distance = %s y_distance = %s, angular = %s'%(x,y,yaw))
        if x == 0.0 and y == 0:
            self.accurate_turn_an_angular.turn(self.cal_now_pose_to_pose(yaw))
        else:
            self.start_run(x, y,self.cal_now_pose_to_pose(yaw))

    def cal_now_pose_to_pose(self,goal_pose_yaw):
        current_yaw = self.robot_state.get_robot_current_w()
        return self.normalize_angle(current_yaw - goal_pose_yaw)
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592

    def normalize_angle(self, angle):
    # 将目标角度转换成-pi到pi之间
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        print('current angular is %s'%angle)
        return  angle

if __name__ == '__main__'   :
    rospy.init_node('linear_move')
    move_cmd = linear_move()
<<<<<<< HEAD
<<<<<<< HEAD
    print self.cal_now_pose_to_pose(1.57)
#move_cmd.move_to( x = 3.6 ,y =2.4,yaw =  3.14  )
=======
    move_cmd.move_to( x = 2.4 ,y =0.0,yaw = 0.0)
#    rospy.sleep(1.0)
#    move_cmd.move_to(x = 1, yaw= 1.57)
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
    move_cmd.move_to( x = 2.4 ,y =0.0,yaw = 0.0)
#    rospy.sleep(1.0)
#    move_cmd.move_to(x = 1, yaw= 1.57)
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592

sys.path.remove(config.robot_state_pkg_path)
