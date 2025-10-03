import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 
from checkerboard_msgs.msg import Corners


class CornerPublisher(Node):

    def __init__(self):
        super().__init__('Corners_publisher')
        self.subscriber = self.create_subscription(Image, 'webcam', self.image_callback)
        self.publisher = self.create_publisher(Image, 'corners', 10)
        self.bridge = CvBridge()
    
    def image_callback(self, msg: Image):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding= 'bgr8')
    
        

        msg.data = self.check_checkerboard(img, rval)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    
    def check_checkerboard(self, img, rval):
        print('Hi from my_package.')

            #grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey = img
        ret, corners = cv2.findChessboardCorners(grey, (3,3), None)
        corner2 = Corners(corner1 = corners[0,0], corner2 = corners[2,0 ], corner3 = corners[8,0 ], corner4 = corners[6, 0])
        return corner2
    #TODO - Implement this once
def main(args=None):
    try:
        with rclpy.init(args=args):
            image_publisher = CornerPublisher()

            rclpy.spin(image_publisher)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


        
