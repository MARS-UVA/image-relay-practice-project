import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImageReaderNode(Node):
    def __init__(self, **kwargs):
        super().__init__("image_reader", **kwargs)
        self.publisher = self.create_publisher(Image, "webcam", 10)
        self.capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
        self.cv_bridge = CvBridge()
        self.timer = self.create_timer(1/15, self.publish_frame)
    
    def publish_frame(self):
        ret, frame = self.capture.read()
        if ret:
            image_msg = self.cv_bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher.publish(image_msg)

    def destroy_node(self):
        super().destroy_node()
        self.capture.release()
        

def main():
    print('Hi from image.')
    rclpy.init()
    node = ImageReaderNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()