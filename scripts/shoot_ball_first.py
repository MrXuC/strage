#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author rescuer xu
#投篮项目1状态机：
#流程：机器前往投篮区域（并放下铲子）-> 检测定位柱 -> 对准定位柱 -> 投篮 -> 前进到中间置球区附近 -> 开始检测球（以原地自转的方式） -> 检测到球后接近球到球前方1米处
#      -> 再次检测球并调整铲子方向后前进  -> 铲球 -> 前进到投篮区域（定位柱附近） -> 检测定位柱 -> 对准定位柱 -> 投篮



import rospy
import smach
import math
import smach_ros
from robot_state_class.second_project_state import *


def shoot_first():
    rospy.init_node('shootBall_first')

    sm_top = smach.StateMachine(outcomes=['successed', 'failed'])
    sm_top.userdata.ball_location_x = 0
    sm_top.userdata.ball_location_y = 0
    sm_top.userdata.ball_theta = 0
    sm_top.userdata.column_x = 0
    sm_top.userdata.column_theta = 0
    with sm_top:

        start = smach.Concurrence(outcomes=['successed','failed'],
                                   default_outcome='failed',
                                   outcome_map={'successed':
                                       { 'SHOVEL_CONTROL_DOWN':'successed',
                                         'MOVE_POINT_PRO_1':'successed'}})

        smach.StateMachine.add("START",start,
                               transitions={"successed":"FIND_COLUMN1",
                                            "failed":"failed"})
        with start:
            smach.Concurrence.add("SHOVEL_CONTROL_DOWN",Shovel_Control_Down())



            smach.Concurrence.add("MOVE_POINT_PRO_1",Move_Point_To_Shoot())


        smach.StateMachine.add('FIND_COLUMN1',Find_Column(),
                               transitions={'successed':'SHOOT_ADJUST1',
                                            'failed':'failed'},
                                        remapping={'column_x': 'column_x',
                                                  'column_theta': 'column_theta'})
        smach.StateMachine.add('SHOOT_ADJUST1',Shoot_Adjust(),
                               transitions={'successed':'SHOOT1',
                                            'failed':'failed'},
                                        remapping={'column_x': 'column_x',
                                                  'column_theta': 'column_theta'})

        smach.StateMachine.add('SHOOT1',Shoot(),
                               transitions={'successed':'ADJUST1',
                                            'failed':'failed'})

        smach.StateMachine.add('ADJUST1',Move_To_Find_Ball(),
                               transitions={'successed':'FindBall',
                                            'failed':'failed'})

        smach.StateMachine.add("FindBall", Search_Ball(),
                               transitions={"successed": "MOVE_POINT",
                                            "failed": "failed"},
                               remapping={'ball_x': 'ball_location_x',
                                          'ball_y': 'ball_location_y',
                                          'ball_theta': 'ball_theta'})

        smach.StateMachine.add('MOVE_POINT',Move_Point(),
                                       transitions={'successed': 'MOVE_ADJUST',
                                                    'failed': 'failed'},
                                       remapping={'ball_x': 'ball_location_x',
                                                  'ball_y': 'ball_location_y',
                                                  'ball_theta': 'ball_theta'})

        smach.StateMachine.add("MOVE_ADJUST",Move_Adjust(),
                               transitions={"successed":"SHOVEL",
                                            "failed":"failed"})

        smach.StateMachine.add('SHOVEL',Shovel(),
                                       transitions={'successed': 'ADJUST2',
                                                    'failed': 'failed'})

        smach.StateMachine.add('ADJUST2',Adjust_To_Shoot(),
                               transitions={'successed':'FIND_COLUMN2',
                                            'failed':'failed'})

        smach.StateMachine.add('FIND_COLUMN2',Find_Column(),
                               transitions={'successed':'SHOOT_ADJUST2',
                                            'failed':'failed'},
                                        remapping={'column_x': 'column_x',
                                                  'column_theta': 'column_theta'})
        smach.StateMachine.add('SHOOT_ADJUST2',Shoot_Adjust(),
                               transitions={'successed':'SHOOT2',
                                            'failed':'failed'},
                                        remapping={'column_x': 'column_x',
                                                  'column_theta': 'column_theta'})

        smach.StateMachine.add('SHOOT2',Shoot(),
                               transitions={'successed':'successed',
                                            'failed':'failed'})


    sm_top.execute()


if __name__ == '__main__':
    shoot_first()