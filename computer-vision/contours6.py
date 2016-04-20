import numpy as np
import cv2

path = "/Users/dongdong/Desktop/3.jpg"

cap = cv2.VideoCapture(path)
fgbg = cv2.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


