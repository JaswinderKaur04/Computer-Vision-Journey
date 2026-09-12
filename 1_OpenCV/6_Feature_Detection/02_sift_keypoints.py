# SIFT (Scale-Invariant Feature Transform).
# SIFT detects a keypoint and assigns it a dominant orientation based on the local gradient directions
# around that keypoint.
# Harris mainly looks for corners.

# SIFT goes further. It tries to find distinctive keypoints that remain useful even when the image is:

# resized (scale changes)
# rotated
# somewhat changed in brightness
# viewed with some variation


import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("original_img.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and calculate descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw keypoints
output = cv2.drawKeypoints(
    gray,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Print information
print("Number of keypoints:", len(keypoints))
print("Descriptor shape:", descriptors.shape)

# Display
plt.imshow(output, cmap="gray")
plt.title("SIFT Keypoints")
plt.axis("off")
plt.show()


# The circle size represents the scale at which SIFT detected that feature.

# What about the lines inside the circles?

# Those indicate the orientation assigned to the keypoint.

# For example:

#      ○
#       \
#        \

# SIFT determines an orientation for the feature based on local image gradients.

# This helps SIFT handle rotation.
# Orientation simply means:
# Which direction is the dominant intensity change around a keypoint.


# Keypoints = important/distinctive locations found by SIFT.

# Descriptors = numerical information describing the appearance around each keypoint.

