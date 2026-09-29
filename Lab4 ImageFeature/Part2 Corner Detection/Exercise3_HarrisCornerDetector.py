# Exercise 3: Harris Corner Detector
# 1. Objective: Understand and implement corner detection techniques using Harris Corner Detector.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply the corner detection using cv2.cornerHarris().
# o Apply the dilation function to mark the corners using cv2.dilate().
# o Save the image.
import cv2
import numpy as np

#Load the image (keep color version + grayscale version separately)
img = cv2.imread("checkerboard.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_float = np.float32(gray)

#Applying the function
#Image – The source image to detect the features
#Dest – Variable to store the output image
#Block size – Neighborhood size
#Ksize – Aperture parameter
#Border type: The pixel revealing type.
dst = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

# dilate to mark the corners
dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 255, 0]

#Display the image
cv2.imshow("harriscornercheckerboard", img)
#Save the image
cv2.imwrite("harriscornercheckerboard.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()