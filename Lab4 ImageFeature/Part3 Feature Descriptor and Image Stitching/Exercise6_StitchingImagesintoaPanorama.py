# Exercise 6: Stitching Images into a Panorama
# 1. Objective: Understand and implement image stitching technique to create a panorama.
# 2. Instructions:
# o Load several images.
# o Call the stitching technique using cv2.Stitcher.create().
# o Stitch the images using stitch().
# o Save the image.
import cv2

#Load images
img1 = cv2.imread("left.jpg")
img2 = cv2.imread("right.jpg")

#Initialized a list of images
images = [img1, img2]

#Call the stitching technique using cv2.Stitcher.create()
stitcher = cv2.Stitcher.create()

#Stitch the images using stitch()
status, panorama = stitcher.stitch(images)

#Display the image
cv2.imshow("panorama", panorama)
#Save the image
cv2.imwrite("panorama.jpg", panorama)

cv2.waitKey(0)
cv2.destroyAllWindows()