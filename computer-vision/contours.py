import numpy as np
import cv2

#path = "/Users/dongdong/Desktop/3.jpg"
#path = "/Users/dongdong/Desktop/5.jpg"
path = "holes.png"

im = cv2.imread(path)

print im.shape #check if the image is loaded correctly
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(0,255,0),3)

cv2.imshow("contours title", im)
cv2.imwrite('contours.png',im)
cv2.waitKey()

