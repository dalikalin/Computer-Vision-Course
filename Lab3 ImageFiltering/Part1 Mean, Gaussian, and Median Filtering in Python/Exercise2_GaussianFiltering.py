# Exercise 2: Gaussian Filtering
# 1. Objective: Recognize how Gaussian smoothing reduces noise while preserving edges.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply a Gaussian filtering with a 5x5 kernel and σ=1 using cv2.GaussianBlur().
# o Save the image.
import cv2

#Load an image in grayscale
img = cv2.imread("lena.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Gaussian filtering
gaussianfiltering = cv2.GaussianBlur(img, (5 , 5), 1)

#Display the image
cv2.imshow("gaussianfilteringlena", gaussianfiltering)
#Save the image
cv2.imwrite("gaussianfilteringlena.png", gaussianfiltering)

cv2.waitKey(0)
cv2.destroyAllWindows()