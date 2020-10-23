cmake_minimum_required(VERSION 2.8.3)
project(dnb_word_counter)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  dnb_msgs
)

add_service_files(
  FILES
  CountWords.srv
)

generate_messages( DEPENDENCIES std_msgs )

catkin_package( CATKIN_DEPENDS message_runtime dnb_msgs)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
