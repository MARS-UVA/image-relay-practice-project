import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class TiltNode(Node):

    def __init__(self, **kwargs):
        super().__init__("tilt_node", **kwargs)


def main() -> None:
    rclpy.init()
    try:
        node = TiltNode()
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()



