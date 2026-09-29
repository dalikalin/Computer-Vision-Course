# Exercise 3: Median Filtering
# 1. Objective: Learn how median filtering effectively removes salt-and-pepper noise.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply a Median filtering with a 3x3 kernel using cv2.medianBlur().
# o Save the image.
import cv2

#Load an image in grayscale
img = cv2.imread("lena.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Median filtering
medianfiltering = cv2.medianBlur(img, 3)

#Display the image
cv2.imshow("medianfilteringlena", medianfiltering)
#Save the image
cv2.imwrite("medianfilteringlena.png", medianfiltering)

cv2.waitKey(0)
cv2.destroyAllWindows()