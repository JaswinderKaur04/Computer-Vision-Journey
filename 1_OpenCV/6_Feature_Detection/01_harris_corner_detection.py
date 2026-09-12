# The fundamental idea

# Harris asks:

# "If I move a small window around this point, how much does the image change?"

# This gives us three cases:

#                   Pixel/Region
#                        │
#           ┌────────────┼────────────┐
#           ↓            ↓            ↓
#         Flat          Edge        Corner
#           │            │            │
#        No change    Change in    Change in
#                     one direction two directions
#           │            │            │
#           ↓            ↓            ↓
#        Not useful    Edge        Strong feature

            # Canny
            #   ↓
            # "Where are the edges?"

            # Contours
            #   ↓
            # "Which edges form object boundaries?"

            # Harris
            #   ↓
            # "Where are the corners?"

            # SIFT / ORB
            #   ↓
            # "Which locations are distinctive enough
            # to recognize and match?"
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("original_img.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Harris corner detection
corners = cv2.cornerHarris(
    gray,
    2,    #blockSize LOCAL REGION Use gradient information "Does this region look like a corner?"
    3,    #ksize → kernel size (calculates intensity changes),Sobel kernel
    0.04  #k controls the sensitivity of the Harris corner response.Typical values are often around:0.04 – 0.06
)

# Dilate corners to make them visible
corners = cv2.dilate(corners, None)

# Mark strong corners
img[corners > 0.01 * corners.max()] = [0, 0, 255]
# THRESHOLD
# 0.01 → many corners
# 0.05 → fewer corners
# 0.10 → very few strong corners

# Display
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Harris Corner Detection")
plt.axis("off")
plt.show()