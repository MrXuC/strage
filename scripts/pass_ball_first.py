#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author rescuer xu

#传球项目1状态机：
#流程：机器前往传球区并放下铲子 -> 传球 -> 前进到找球的位置 -> 开始检测球（以原地自转的方式） -> 检测到球后接近球到球前方1米处
#      -> 再次检测球并调整铲子方向后前进  -> 铲球 -> 调整机器角度朝向传球区 -> 投球 -> 升起铲子 -> 回家

import rospy
import smach
import math
import smach_ros
from robot_state_class.first_project_state import *


def pass_first():
    rospy.init_node('passBall_first')
    rospy.loginfo("!!!!!!!!!!!!!!!!!!!!!!!!!")
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
                                         'MOVE_POINT_TO_SHOOT':'successed'}})


        with start:
            smach.Concurrence.add("SHOVEL_CONTROL_DOWN",Shovel_Control_Down())

            smach.Concurrence.add('MOVE_POINT_TO_SHOOT',Move_Point_To_Shoot())


        smach.StateMachine.add("START",start,
                               transitions={"successed":"SHOOT1",
                                            "failed":"failed"})

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

        smach.StateMachine.add('ADJUST2',Shoot_Adjust(),
                               transitions={'successed':'SHOOT2',
                                            'failed':'failed'})

        smach.StateMachine.add('SHOOT2',Shoot(),
                               transitions={'successed':'SHOVEL_CONTROL_UP',
                                            'failed':'failed'})

        smach.StateMachine.add("SHOVEL_CONTROL_UP",Shovel_Control_Up(),
                               transitions={"successed":"RETURN",
                                            "failed":"failed"})

        smach.StateMachine.add('RETURN',Return(),
                               transitions={'successed':'successed',
                                                              'failed':'failed'})

    sm_top.execute()

if __name__ == '__main__':
    pass_first()