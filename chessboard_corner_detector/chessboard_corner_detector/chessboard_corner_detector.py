import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ChessboardCornerDetector(Node):
    def __init__(self, **kwargs):
        super().__init__("chessboard_corner_detector", **kwargs)
        self.pattern_size = (7, 7)
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.bridge = CvBridge()
        # Subscribe to camera images
        self.subscription = self.create_subscription(
            Image,
            "webcam",
            self.image_callback,
            10
        )
    
    def image_callback(self, msg):
        # Convert ROS image to OpenCV
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, self.pattern_size, None)

        if ret:
            corners_subpix = cv2.cornerSubPix(
                gray, corners, (11, 11), (-1, -1), self.criteria
            )

            cv2.drawChessboardCorners(frame, self.pattern_size, corners_subpix, ret)
            self.get_logger().info("Chessboard corners found!")

        else:
            self.get_logger().warn("Chessboard not found in this frame.")

        # Show debug window (optional)
        cv2.imshow("Chessboard Detector", frame)
        cv2.waitKey(1)

def main(args=None):
    print('Chessboard corner detector is running!')
    rclpy.init(args=args)
    node = ChessboardCornerDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()