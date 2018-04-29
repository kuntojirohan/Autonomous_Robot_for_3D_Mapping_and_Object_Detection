#! /usr/bin/env python

import rospy
import cv2
import cv2.cv as cv
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import numpy as np



def Imagecallback(ros_image):
    try:
		bridge = CvBridge()
		frame = bridge.imgmsg_to_cv2(ros_image, "8UC1")
		frame = np.array(frame, dtype=np.uint8)
		cv2.imshow('frame', frame)
		cv.WaitKey(1)
    except:
		cv2.DestryAllWindows()




if __name__ == '__main__':
    try:
        rospy.init_node("Edge_detetcion")
        image_sub = rospy.Subscriber("/kinect2/sd/image_ir", Image, Imagecallback)
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down vision node."
        cv.DestroyAllWindows()
