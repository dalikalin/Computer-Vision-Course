# Exercise 4: Image Rotation
# 1. Objective: Rotate an image around its center using OpenCV.
# 2. Instructions:
# o Load an image.
# o Get the image center.
# o Compute rotation matrix using cv2.getRotationMatrix2D().
# o Apply the rotation using cv2.warpAffine() while keeping the same width and height of the image.
# o Save the image.
import cv2

#Load the image
img = cv2.imread("sheldon.jpg")

#Get the image center
h, w = img.shape[:2]
center = (w // 2, h // 2)

#Compute rotation matrix
angle = 45
rotation = cv2.getRotationMatrix2D(center, angle, 1.0)

#Apply the rotation
rotatedsheldon = cv2.warpAffine(img, rotation, (w,h))

#Display the image
cv2.imshow("rotatedsheldon", rotatedsheldon)

#Save the image
cv2.imwrite("rotatedsheldon.jpg", rotatedsheldon)


cv2.waitKey(0)
cv2.destroyAllWindows()

