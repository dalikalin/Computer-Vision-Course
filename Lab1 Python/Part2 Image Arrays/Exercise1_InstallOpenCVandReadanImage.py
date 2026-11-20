# Exercise 1: Install OpenCV and Read an Image
# 1. Objective: Learn how to install OpenCV and read an image from disk.
# 2. Instructions:
#   o Install OpenCV using pip: pip install opencv-python.
#   o Import OpenCV in your script.
#   o Load an image (e.g., a sample .jpg file) from your computer using OpenCV’s cv2.imread() function.
#   o Display the image in a window using cv2.imshow().
#   o Close the window when a key is pressed using cv2.waitKey() and cv2.destroyAllWindows().

import cv2
img = cv2.imread("drstrange.jpg")
cv2.imshow("Doctor Strange", img)
cv2.waitKey(0)
cv2.destroyAllWindows()