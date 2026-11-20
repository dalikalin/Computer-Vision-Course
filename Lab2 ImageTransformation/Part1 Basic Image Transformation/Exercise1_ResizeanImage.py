# Exercise 1: Resize an Image
# 1. Objective: Learn how to resize an image using OpenCV.
# 2. Instructions:
# o Load an image.
# o Resize it to specific size using cv2.resize().
# o Save the image.
import cv2

#Load an image
img = cv2.imread("sheldon.jpg")

#Resize
resized = cv2.resize(img, (400, 400))

#Display the image
cv2.imshow("resizedsheldon", img)

#Save the image
cv2.imwrite("resizedsheldon.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()