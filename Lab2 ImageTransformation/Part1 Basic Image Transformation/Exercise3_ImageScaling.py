# Exercise 3: Image Scaling
# 1. Objective: Learn how to scale an image using OpenCV.
# 2. Instructions:
# o Load an image.
# o Scale the image down by 50% using cv2.resize().
# o Save the image.
# o Scale the image up by 150%.
# o Save the image.
import cv2

#Load image
img = cv2.imread("sheldon.jpg")

#Scale down the image by 50%
scaleddownsheldon = cv2.resize(img, None, fx=0.5, fy=0.5)
#Scale up the image by 150%
scaledupsheldon = cv2.resize(img, None, fx=1.5, fy=1.5)

#Display the image
cv2.imshow("scaleddownsheldon", scaleddownsheldon)
cv2.imshow("scaledupsheldon", scaledupsheldon)
#Save the image
cv2.imwrite("scaleddownsheldon.jpg", scaleddownsheldon)
cv2.imwrite("scaledupsheldon.jpg", scaledupsheldon)

cv2.waitKey(0)
cv2.destroyAllWindows()