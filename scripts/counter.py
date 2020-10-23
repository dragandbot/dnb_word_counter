#!/usr/bin/env python

import rospy

from dnb_word_counter.srv import *
from dnb_msgs.msg import *

def handle(request):
	text = request.text
	response = CountWordsResponse()
	response.words = len(text.split(" ")) + int(rospy.get_param('~offset', "0" ))
	return response

if __name__ == "__main__":
	rospy.init_node('word_counter')
	rospy.Service('~count_words', CountWords, handle)

	pub_component_status = rospy.Publisher('~status', ComponentStatus, queue_size=1, latch=True)
	
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		cm_status = ComponentStatus()
		cm_status.status_id = ComponentStatus().RUNNING
		pub_component_status.publish(cm_status)
		rate.sleep()
