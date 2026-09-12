import cv2
import matplotlib.pyplot as plt

# Read images
img1 = cv2.imread("original_img.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("cropped_img.jpg", cv2.IMREAD_GRAYSCALE)

# Create ORB detector
orb = cv2.ORB_create(nfeatures=500)

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
print("____________________________",kp1)
# Print information
print("Image 1 keypoints:", len(kp1))
print("Image 2 keypoints:", len(kp2))

print("Image 1 descriptor shape:", des1.shape)
print("Image 2 descriptor shape:", des2.shape)
