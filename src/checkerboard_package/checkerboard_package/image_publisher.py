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
        
        #-----------------------------------------
        #TEMPORARY REPLACE WITH ROS MESSAGE LATER
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)
        if vc.isOpened(): # try to get the first frame
            rval, img = vc.read()
        else:
            rval = False
        rval, img = vc.read()
        #-----------------------------------------

        msg.data = self.check_checkerboard(img, rval)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    
    def check_checkerboard(img, rval):
        print('Hi from my_package.')

        while rval:
            #grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            rval, img = get_frame_from_ros()
            grey = img
            file_thing = open("testfile.txt", "a")
            ret, corners = cv2.findChessboardCorners(grey, (3,3), None)

            top_left, top_right, bottom_right, bottom_left  = 0,0,0,0

            
            if ret == True:
                print("-------------------")
                send_to_node(corners)
                file_thing.write(str(corners)+"\n")
                file_thing.close()
            img = cv2.drawChessboardCorners(grey, (3,3), corners,ret)
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
            cv2.imshow("preview", img)
            #time.sleep(1)
        return corners
    

    def main(args=None):
        try:
            with rclpy.init(args=args):
                image_publisher = ImagePublisher()

                rclpy.spin(image_publisher)
        except (KeyboardInterrupt, ExternalShutdownException):
            pass
        
