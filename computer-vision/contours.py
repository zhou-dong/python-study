import numpy as np
import cv2
import sys

fileName = sys.argv[1]
imageName = fileName.split(".")[0]
path = fileName

print path
im = cv2.imread(path)

print im.shape #check if the image is loaded correctly
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(0,255,0),3)

nameContour =  imageName + "_contour.png"
cv2.imshow("contours title", im)
cv2.imwrite(nameContour,im)

while True:
     ch = cv2.waitKey()
     if ch == 27:
         break
cv2.destroyAllWindows()
