# Exercise 4: Sobel Edge Detection
# 1. Objective: Understand and implement edge detection techniques using Sobel filter.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply Sobel edge detection for both X and Y directions using cv2.Sobel().
# o Combine the Sobel X and Y results to get the final edges using cv2.magnitude().
# o Save the image.
import cv2

#Load an image in grayscale
img = cv2.imread("drdoom.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply sobel
# X direction
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# Y direction
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# Combine Sobel X and Y
sobelcombined = cv2.magnitude(sobelx, sobely)

#Converts the values back into the normal 0–255
sobelcombined = cv2.convertScaleAbs(sobelcombined)

#Display the image
cv2.imshow("sobeldrdoom", sobelcombined)
#Save the image
cv2.imwrite("sobeldrdoom.jpg", sobelcombined)

cv2.waitKey(0)
cv2.destroyAllWindows()