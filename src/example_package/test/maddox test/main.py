import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, img = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", img)
    rval, img = vc.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(grey, (3,3), None)
    print(corners)
    img = cv2.drawChessboardCorners(grey, (3,3), corners,ret)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break


cv2.destroyWindow("preview")
vc.release()