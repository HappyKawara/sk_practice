#!/usr/bin/env python
# -*- cording: utf-8 -*-

import rospy
from happymimi_voice_msgs.srv import StringToString
from happymimi_voice_msgs.srv import StringToStringResponse

req = "avian"
ge = rospy.ServiceProxy('/gender_jg',StringToString)
x = ge(req)
if x.result:
    print(x.result_data)


