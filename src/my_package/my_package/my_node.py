import cv2

def main():
    print('Hi from my_package.')
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, img = vc.read()
    else:
        rval = False

    #TODO: Make this actually send to a ROS node
    def send_to_node(data):
        print(data)

    def get_frame_from_ros():
        rval, img = vc.read()
        return rval, img



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


    cv2.destroyWindow("preview")
    vc.release()


if __name__ == '__main__':
    main()
