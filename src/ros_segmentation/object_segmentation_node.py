#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Empty
from visualization_msgs.msg import Marker
import cv_bridge
import mask_rcnn
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
model_path = rospy.get_param('~model_path')
classes_path = rospy.get_param('~classes_path')


class ObjectDetectionNode:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)
        self.image_pub = rospy.Publisher("/processed_image", Image, queue_size=1)
        self.stop_pub = rospy.Publisher("/stop", Empty, queue_size=1)
        self.marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size=1)
        self.mask_rcnn = mask_rcnn.MaskRCNN()

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        boxes, classes, contours, centers = self.mask_rcnn.detect_objects_mask(cv_image)
        processed_image = self.mask_rcnn.draw_object_mask(cv_image)
        processed_image_msg = self.bridge.cv2_to_imgmsg(processed_image, "bgr8")
        self.image_pub.publish(processed_image_msg)
        if len(boxes) > 0:
            self.stop_pub.publish(Empty())
            marker = Marker()
            # Fill in the marker values
            self.marker_pub.publish(marker)

if __name__ == '__main__':
    rospy.init_node('object_detection_node')
    node = ObjectDetectionNode()
    rospy.spin()

#   <node pkg="turtlebot3" type="object_segmentation_node" name="object_segmentation_node" output="screen">
#     <param name="model_path" value="/home/justin/turtlebot3/src/turtlebot3/semantic_segmentation/dnn/frozen_inference_graph_coco.pb" />
#     <param name="classes_path" value="/home/justin/turtlebot3/src/turtlebot3/semantic_segmentation/dnn/classes.txt" />
#   </node>