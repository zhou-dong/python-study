import numpy as np
import cv2
import sys

def get_contrasted(image, type="dark", level=3):
    maxIntensity = 255.0 # depends on dtype of image data
    phi = 1
    theta = 1

    if type == "light":
        newImage0 = (maxIntensity/phi)*(image/(maxIntensity/theta))**0.5
        newImage0 = np.array(newImage0,dtype='uint8')
        return newImage0
    elif type == "dark":
        newImage1 = (maxIntensity/phi)*(image/(maxIntensity/theta))**level
        newImage1 = np.array(newImage1,dtype='uint8')
        return newImage1

def sharp(image, level=3):
    f = cv2.GaussianBlur(image, (level,level), level)
    f = cv2.addWeighted(image, 1.5, f, -0.5, 0)
    return f

grades = ['a', 'b', 'c']
path = sys.argv[1]
grade = sys.argv[2]

if grade not in grades:
    raise Exception('grade only can be a, b or c')
imageName = path.split(".")[1]

original_image = cv2.imread(path)
# 1 Convert to gray & Normalize
gray_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
gray_img = sharp(get_contrasted(gray_img))

# 2 Find Threshold
gray_blur = cv2.GaussianBlur(gray_img, (7, 7), 0)
adapt_thresh_im = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
max_thresh, thresh_im = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
thresh = cv2.bitwise_or(adapt_thresh_im, thresh_im)

# 3 Dilate
gray = cv2.Canny(thresh, 88, 400, apertureSize=3)
gray = cv2.dilate(gray, None, iterations=8)
gray = cv2.erode(gray, None, iterations=8)

# 4 Flood
contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_info = []
for c in contours:
    contour_info.append((
        c,
        cv2.isContourConvex(c),
        cv2.contourArea(c),
    ))
contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
max_contour = contour_info[0]
holes = np.zeros(gray_img.shape, np.uint8)
cv2.drawContours(holes, max_contour, 0, 255, -1)
cv2.imwrite("holes.png",holes)

im = cv2.imread("holes.png")

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(0,255,0),3)

cv2.imwrite("holes.png",im)

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
        if (index != 0 and index % thread == 0 ):
            score.append(margin)
        if (margin < 10):
            continue
        if (index > 10 and margin < minimum):
            minimum = margin
            minimumIndex = index
        if (index > 10 and maximum < margin):
            maximum = margin
            maximumIndex = index

iteratorLine()

score[:] = [x / float(minimum) for x in score]

dataFile = open("data.txt", "a")

for x in score:
    dataFile.write(str(x) + " ")
dataFile.write(grade)
dataFile.write("\n")
dataFile.close()

cv2.destroyAllWindows()

print "analyze data finish..."
