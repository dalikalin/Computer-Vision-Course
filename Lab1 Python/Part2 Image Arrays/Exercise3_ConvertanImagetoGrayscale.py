# Exercise 3: Convert an Image to Grayscale
# 1. Objective: Learn how to modify an image by converting it to grayscale.
# 2. Instructions:
# o Load an image.
# o Convert it to grayscale using cv2.cvtColor() with the flag cv2.COLOR_BGR2GRAY.
# o Display and/or save the grayscale image.
import cv2
img = cv2.imread("drstrange.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("graydrstrange", gray)
cv2.imwrite("graydrstrange.jpg", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()