cmake_minimum_required(VERSION 2.8.3)
project(basketball_strage)

find_package(catkin REQUIRED COMPONENTS
  basketball_msgs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
#  ros_smach
=======
  smach_ros
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
  smach_ros
>>>>>>> d41aa20b485db43a3c212e87195b10342618c153
=======
#  ros_smach
>>>>>>> c23cd36a28263fa7e748e644f0229d201acd5592
  roscpp
  rospy
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES basketball_strage
#  CATKIN_DEPENDS basketball_msgs ros_smach roscpp rospy
#  DEPENDS system_lib
)



## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


