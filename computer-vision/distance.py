import numpy as np
import cv2

#path = "holes.png"
path = "contours.png"

source = cv2.imread(path)
im = np.copy(source)

x = len(im[:,1])
y = len(im[1,:])


def leftMost(line):
    for index, pix in enumerate(line):
        if pix[1]==255:
            return index
    return -1 ;

def rightMost(line):
    index = y-1
    for pix in reversed(line):
        if pix[1] == 255:
            return index
        index -= 1
    return -1 ;

def iteratorLine():
    global im
    font = cv2.FONT_HERSHEY_SIMPLEX
    for index, line in enumerate(im):
        margin = rightMost(line) - leftMost(line)
        cv2.line(im,(0,index),(y,index),(255,255,0),2)
        cv2.putText(im, str(margin),(100,index), font, 1,(255,255,255),2)
        cv2.imshow("Holes", im)
        cv2.waitKey(1)
        im = np.copy(source)

cv2.destroyAllWindows()

iteratorLine()
