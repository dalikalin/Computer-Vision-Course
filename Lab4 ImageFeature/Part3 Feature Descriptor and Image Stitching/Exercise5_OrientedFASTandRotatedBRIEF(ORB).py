# Exercise 5: Oriented FAST and Rotated BRIEF (ORB)
# 1. Objective: Understand and implement feature descriptors techniques using ORB.
# 2. Instructions:
# o Load an image in grayscale.
# o Apply the feature descriptor using cv2.ORB_create().
# o Apply the features matching using detectAndCompute().
# o Draw keypoints using cv2.drawKeypoints().
# o Save the image.
import cv2

#Load an image in grayscale
img = cv2.imread("lena.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Descriptor
orb = cv2.ORB_create(nfeatures=1000)

#Features matching
keypoints_orb, descriptors = orb.detectAndCompute(img, None)

#Draw keypoints
imgorb = cv2.drawKeypoints(img, keypoints_orb, None)

#Display the image
cv2.imshow("orblena", imgorb)
#Save the image
cv2.imwrite("orblena.png", imgorb)

cv2.waitKey(0)
cv2.destroyAllWindows()