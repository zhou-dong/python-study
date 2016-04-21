import numpy as np
import cv2

#path = "holes.png"
path = "contours.png"

m = np.array(cv2.imread(path))

print m.shape

x = len(m[:,1])
y = len(m[1,:])

row1 = m[3,:]
for pix in row1:
    print pix


print m[1:1]
