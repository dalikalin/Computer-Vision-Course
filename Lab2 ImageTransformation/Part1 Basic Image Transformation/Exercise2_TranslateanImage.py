# Exercise 2: Translate an Image
# 1. Objective: Learn how to translate an image using OpenCV.
# 2. Instructions:
# o Load an image.
# o Shift an image 100 pixels to the right and 50 pixels down using cv2.warpAffine().
# o Save the image.
import cv2
import numpy as np

#Load the image
img = cv2.imread("sheldon.jpg")

h, w = img.shape[:2]

#Define the translation matrix (2x3)[1, 0, tx][0, 1, ty]
#shift right by 100, down by 50
translationmatrix = np.float32([[1, 0, 100], [0, 1, 50]])

#Apply the translation
translatedimage = cv2.warpAffine(img, translationmatrix, (w, h))

#Display the image
cv2.imshow("translatedimage", translatedimage)
#Save the image
cv2.imwrite("translatedsheldon.jpg", translatedimage)

cv2.waitKey(0)
cv2.destroyAllWindows()