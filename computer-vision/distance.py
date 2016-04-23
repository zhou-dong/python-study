import numpy as np
import cv2

#path = "holes.png"
path = "./img/contours.png"

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
    minimum = 100000000 
    maximum = 0
    temp = 0
    minimumIndex = 0
    maximumIndex = 0
    for index, line in enumerate(im):
        margin = rightMost(line) - leftMost(line)
        drawLine(line, margin, index)
        if(margin < 10):
            continue
        if(index > 200 and index< 500 and margin < minimum):
            minimum = margin
            minimumIndex = index
        if(index > 200 and maximum < margin):
            maximum = margin
            maximumIndex = index
    drawMinMax(minimumIndex, maximumIndex, minimum, maximum, im)

def drawMinMax(minimumIndex, maximumIndex, minimum, maximum, im):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.line(im,(0,minimumIndex),(len(im[1,:]),minimumIndex),(255,255,0),2)
    cv2.line(im,(0,maximumIndex),(len(im[1,:]),maximumIndex),(255,255,0),2)
    cv2.putText(im, str(minimum),(100,minimumIndex), font, 1,(255,255,255),2)
    cv2.putText(im, str(maximum),(100,maximumIndex), font, 1,(255,255,255),2)
    cv2.imshow("Holes", im)
    cv2.waitKey(20000)

def drawLine(line, margin, index):
    global im
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.line(im,(0,index),(len(im[1,:]),index),(255,255,0),2)
    cv2.putText(im, str(margin),(100,index), font, 1,(255,255,255),2)
    cv2.imshow("Holes", im)
    cv2.waitKey(1)
    im = np.copy(source)

cv2.destroyAllWindows()

iteratorLine()
