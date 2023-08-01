# #!/usr/bin/env python

# import rospy
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# from realsense_camera import RealsenseCamera
# from mask_rcnn import MaskRCNN
# from measure_object_distance import depth_frame
# import sys
# sys.path.insert(0, '/home/justin/realsense_ws/src/realsense-ros/realsense2_camera/src/')

# class SemanticSegmentationNode:
#     def __init__(self):
#         self.bridge = CvBridge()

#         self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)

#         self.semantic_pub = rospy.Publisher("/semantic_image", Image, queue_size=10)

#         # Load Realsense camera
#         self.rs = RealsenseCamera()
#         self.mrcnn = MaskRCNN()

#     def image_callback(self, msg):
#         rospy.loginfo("Received an image!")
#         cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

#         boxes, classes, contours, centers = self.mrcnn.detect_objects_mask(cv_image)

#         cv_image = self.mrcnn.draw_object_mask(cv_image)

#         self.mrcnn.draw_object_info(cv_image, depth_frame)

#         semantic_msg = self.bridge.cv2_to_imgmsg(cv_image, "bgr8")

#         rospy.loginfo("Publishing the semantic image!")
#         self.semantic_pub.publish(semantic_msg)


# if __name__ == "__main__":
#     rospy.init_node("semantic_segmentation_node")
#     node = SemanticSegmentationNode()
#     rospy.spin()
