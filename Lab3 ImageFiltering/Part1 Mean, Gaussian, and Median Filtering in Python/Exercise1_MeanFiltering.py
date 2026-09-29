# Exercise 1: Mean Filtering
# 1. Objective: Understand uniform smoothing and its effect on noise.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply a mean filtering with a 3x3 kernel using cv2.blur().
# o Save the image
import cv2

#Load an image in grayscale
img = cv2.imread("lena.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Mean filtering
meanfilter = cv2.blur(img, (3 , 3))

#Display the image
cv2.imshow("meanfilterlena", meanfilter)
#Save the image
cv2.imwrite("meanfilterlena.png", meanfilter)

cv2.waitKey(0)
cv2.destroyAllWindows()