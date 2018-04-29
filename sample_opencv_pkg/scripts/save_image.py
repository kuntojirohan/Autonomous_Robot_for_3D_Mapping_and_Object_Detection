#! /usr/bin/env python

import rospy
import cv2
import cv2.cv as cv
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import numpy as np


frame = None



def Imagecallback(ros_image):
    global frame
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame = np.array(frame, dtype=np.uint8)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)



try:
    rospy.init_node("Edge_detetcion")
    image_sub = rospy.Subscriber("/kinect2/qhd/image_color", Image, Imagecallback)
    n = 0
    while True:
        x = raw_input("Take_image: ")
        cv2.imwrite('image_%s' %n +'.png', frame)
        n+=1
    rospy.spin()
except KeyboardInterrupt:
    print"Shutting down vision node."
    cv.DestroyAllWindows()


