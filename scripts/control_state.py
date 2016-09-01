#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import rospy
import pass_ball_first
import pass_ball_second
import pass_ball_third
import shoot_ball_first
import shoot_ball_second
import shoot_ball_third
import basketball_msgs.srv as basketball_srv
class main(object):
    def __init__(self):
<<<<<<< HEAD
<<<<<<< HEAD
        self.state = [lambda:    pass_ball_first.pass_first,
                 lambda:    pass_ball_second.pass_second,
                 lambda:    pass_ball_third.pass_third,
                 lambda:    shoot_ball_first.shoot_first,
=======
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
        self.state = [lambda:    pass_ball_first.pass_first ,
                 lambda:    pass_ball_second.pass_second ,
                 lambda:    pass_ball_third.pass_third,
                 lambda:    shoot_ball_first.shoot_first ,
<<<<<<< HEAD
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
                 lambda:    shoot_ball_second.shoot_second ,
                 lambda:    shoot_ball_third.shoot_third  ]
        self.service = rospy.Service('Control_State', basketball_srv.ControlState, self.srv_callback)

    def srv_callback(self,req):
<<<<<<< HEAD
<<<<<<< HEAD
        if req.control_type == 0:
            pass_ball_first.pass_first()
        elif req.control_type == 1:
            pass_ball_second.pass_second()
        elif req.control_type == 2:
            pass_ball_third.pass_third()
        elif req.control_type == 3:
            shoot_ball_first.shoot_first()
        elif req.control_type == 4:
            shoot_ball_second.shoot_second()
        elif req.control_type == 5:
            shoot_ball_third.shoot_third()

=======
        self.state[req.control_type]
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
        self.state[req.control_type]
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
        return basketball_srv.ControlStateResponse(True)

    def main_run(self):
        rospy.init_node('Control_State')
<<<<<<< HEAD
<<<<<<< HEAD
        rospy.spin()


if __name__ == '__main__':
    print "dsadasd"
=======
        while not rospy.is_shutdown:
            rospy.spin()
if __name__ == '__main__':
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
=======
        while not rospy.is_shutdown:
            rospy.spin()
if __name__ == '__main__':
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
    main().main_run()
