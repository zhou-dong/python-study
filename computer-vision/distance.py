import numpy as np
import cv2
import sys

path = sys.argv[1]
grade = sys.argv[2]

source = cv2.imread(path)
im = np.copy(source)

x = len(im[:,1])
y = len(im[1,:])

thread = y / 5
score = []

minimum = 10000000

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
    global minimum
    maximum = 0
    temp = 0
    minimumIndex = 0
    maximumIndex = 0
    for index, line in enumerate(im):
        margin = rightMost(line) - leftMost(line)
        drawLine(line, margin, index)
        if (index != 0 and index % thread == 0 ):
            score.append(margin)
            print margin
        if (margin < 10):
            continue
        if (index > 10 and margin < minimum):
            minimum = margin
            minimumIndex = index
        if (index > 10 and maximum < margin):
            maximum = margin
            maximumIndex = index
    drawMinMax(minimumIndex, maximumIndex, minimum, maximum, im)

def drawMinMax(minimumIndex, maximumIndex, minimum, maximum, im):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.line(im,(0,minimumIndex),(len(im[1,:]),minimumIndex),(255,255,0),2)
    cv2.line(im,(0,maximumIndex),(len(im[1,:]),maximumIndex),(255,255,0),2)
    cv2.putText(im, str(minimum),(10,minimumIndex), font, 1,(255,255,255),2)
    cv2.putText(im, str(maximum),(10,maximumIndex), font, 1,(255,255,255),2)
    cv2.imshow("Holes", im)

def drawLine(line, margin, index):
    global im
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.line(im,(0,index),(len(im[1,:]),index),(255,255,0),2)
    cv2.putText(im, str(margin),(100,index), font, 1,(255,255,255),2)
    cv2.imshow("Holes", im)
    cv2.waitKey(1)
    im = np.copy(source)

iteratorLine()

score[:] = [x / float(minimum) for x in score]

dataFile = open("data.txt", "a")

for x in score:
    dataFile.write(str(x) + " ")
dataFile.write(grade)
dataFile.write("\n")
dataFile.close() 

print score
while True:
    ch = cv2.waitKey()
    if ch == 27:
        break
cv2.destroyAllWindows()

