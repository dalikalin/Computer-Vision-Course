# Exercise 4: Shi-Tomasi Detector
# 1. Objective: Understand and implement corner detection techniques using Shi-Tomasi Detector.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply the corner detection using cv2.goodFeaturesToTrack().
# o Draw each keypoint cv2.circle().
# o Save the image.
import cv2
import numpy as np

#Load the image (keep color version + grayscale version separately)
img = cv2.imread("checkerboard.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Applying the function
#image – The source image we need to extract the features.
#maxc – Maximum number of corners we want [Negative values gives all the corners]
#Quality – Quality level parameter (preferred value=0.01)
#maxD – Maximum distance (preferred value=10)
corners = cv2.goodFeaturesToTrack(gray, maxCorners=30, qualityLevel=0.01, minDistance=10)
corners = np.int32(corners)

for item in corners:
    x, y = item[0]
    x = int(x)
    y = int(y)
    cv2.circle(img, (x, y), 6, (0, 255, 0), -1)

#Display the image
cv2.imshow("shitomasicheckerboard", img)
#Save the image
cv2.imwrite("shitomasicheckerboard.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()