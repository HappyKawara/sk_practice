import rospy
from happymimi_voice_msgs.srv import StringToString

service =rospy.ServiceProxy("/gender_jg",StringToString)
print(service("mike"))
