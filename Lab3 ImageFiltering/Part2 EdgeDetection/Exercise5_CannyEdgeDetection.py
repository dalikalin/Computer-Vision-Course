# Exercise 5: Canny Edge Detection
# 1. Objective: Understand and implement edge detection techniques using Canny filter.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply Canny edge detection using cv2.Canny().
# o Save the image.
import cv2

#Load an image in grayscale
img = cv2.imread("drdoom.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply canny
canny = cv2.Canny(img, 50, 150)

#Display the image
cv2.imshow("cannydrdoom", canny)
#Save the image
cv2.imwrite("cannydrdoom.jpg", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()