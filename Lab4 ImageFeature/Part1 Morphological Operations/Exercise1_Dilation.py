# Exercise 1: Dilation
# 1. Objective: Expand white regions of an image.
# 2. Instructions:
# o Load an image in grayscale.
# o Define the kernel for this operation.
# o Apply the dilation function using cv2.dilate().
# o Save the image
import cv2
import numpy as np

#Load an image in grayscale
img = cv2.imread("bwgirl.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Define the kernel
kernel = np.ones((3, 3), np.uint8)

# The first parameter is the original image, kernel is the matrix with which image is convolved and third parameter is the number of iterations, which will determine how much you want to erode/dilate a given image.
#Apply the dilation function using cv2.dilate()
dilation = cv2.dilate(img, kernel, iterations=1)

#Display the image
cv2.imshow("dilationbwgirl", dilation)
#Save the image
cv2.imwrite("dilationbwgirl.jpg", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()