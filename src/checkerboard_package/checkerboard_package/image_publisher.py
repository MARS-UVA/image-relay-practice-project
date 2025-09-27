import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 
from checkerboard_msgs.msg import Corners


class ImagePublisher(Node):

    def __init__(self):
        super().__init__('Corners image publisher')
        self.publisher = self.create_publisher(Image, 'corners', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = Image()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    

    def main(args=None):
        try:
            with rclpy.init(args=args):
                image_publisher = ImagePublisher()

                rclpy.spin(image_publisher)
        except (KeyboardInterrupt, ExternalShutdownException):
            pass
        
