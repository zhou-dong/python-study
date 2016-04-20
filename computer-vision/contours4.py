import cv
import cv2
import numpy as np
import sys

# Align images with cv2

path = "/Users/dongdong/Desktop/3.jpg" 

imgBack = cv2.imread(path)
imgTest = cv2.imread(path)

detector = cv2.FeatureDetector_create("SURF")
descriptor = cv2.DescriptorExtractor_create("BRIEF")
matcher = cv2.DescriptorMatcher_create("BruteForce-Hamming")

# the matcher works on single channel images
grayBack = cv2.cvtColor(imgBack, cv2.COLOR_RGB2GRAY)
grayTest = cv2.cvtColor(imgTest, cv2.COLOR_RGB2GRAY)

# Compute magic (I found this code elsewhere 
kp1 = detector.detect(grayBack)
kp2 = detector.detect(grayTest)

k1, d1 = descriptor.compute(grayBack, kp1)
k2, d2 = descriptor.compute(grayTest, kp2)

matches = matcher.match(d1, d2)

dist = [m.distance for m in matches]
if len(dist) == 0:
    print "No Suitable matches found!"
    sys.exit(1)

mean_dist = sum(dist) / len(dist)
threshold_dist = mean_dist * 0.5

good_matches = [m for m in matches if m.distance < threshold_dist]

h1, w1 = grayBack.shape[:2]

matches = []
for m in good_matches:
    matches.append((m.queryIdx, m.trainIdx))

if len(good_matches) > 0:
    p1 = np.float32( [k1[i].pt for i, j in matches] )
    p0 = np.float32( [k2[j].pt for i, j in matches] )
    H, mask = cv2.findHomography(p0, p1, cv2.RANSAC)

    output = cv2.warpPerspective(imgTest, H, (w1, h1))
# End Magic

cv2.imwrite("Test-Warped.png", output)

imgBack = cv.LoadImage("Background.png")
imgTest = cv.LoadImage("Test-Warped.png")

diff = cv.CloneImage(imgBack)
grayDiff = cv.CreateImage(cv.GetSize(imgBack), cv.IPL_DEPTH_8U, 1)

# Perform simple substraction    
cv.AbsDiff(imgBack, imgTest, diff)
cv.CvtColor(diff, grayDiff, cv.CV_RGB2GRAY)

# Get our threshold and expand it a little to clean the edges
cv.Threshold(grayDiff, grayDiff, 40, 255, cv.CV_THRESH_BINARY)
cv.Dilate(grayDiff, grayDiff, None, 6)
cv.Erode(grayDiff, grayDiff, None, 2)

# Copy the test image and mask with our threshold
fore = cv.CreateImage(cv.GetSize(imgBack), cv.IPL_DEPTH_8U, 3)
cv.Copy(imgTest, fore, grayDiff)

cv.SaveImage("Threshold.png", grayDiff)
cv.SaveImage("Foreground.png", fore)
