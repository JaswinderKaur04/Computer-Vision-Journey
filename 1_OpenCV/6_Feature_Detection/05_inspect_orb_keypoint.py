import cv2
import matplotlib.pyplot as plt

# Read images
img1 = cv2.imread("original_img.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("cropped_img.jpg", cv2.IMREAD_GRAYSCALE)

# Create ORB detector
orb = cv2.ORB_create(nfeatures=500)

# Detect keypoints and descriptors
kp, des = orb.detectAndCompute(img1, None)
kp = kp[0]
print("Position:", kp.pt)
print("Size:", kp.size)   #size represents the scale/diameter of the keypoint's neighborhood.
print("Angle:", kp.angle)  #This represents the approximate scale/diameter of the neighborhood associated with that keypoint.
print("Response:", kp.response) #How strongly does the ORB detector consider this point to be a useful/distinctive feature?