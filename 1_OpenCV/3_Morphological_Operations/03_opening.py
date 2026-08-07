                        # Threshold Image
                        #         │
                        #         ▼
                        # Small White Noise
                        #         │
                        #         ▼
                        # Erosion
                        #         │
                        #         ▼
                        # Noise Removed
                        # Object Shrinks
                        #         │
                        #         ▼
                        # Dilation
                        #         │
                        #         ▼
                        # Object Restored
                        # Noise Still Gone
                        
# Opening removes small foreground (white) objects while preserving the shape
# of larger objects as much as possible.                        

import cv2
import numpy as np

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)   #The binary image.

# Kernel   The structuring element.
kernel1 = np.ones((3,3), np.uint8)
kernel2 = np.ones((5,5), np.uint8)
kernel3 = np.ones((7,7), np.uint8)

# Opening
opening1 = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel1
)
opening2 = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel2
)

opening3 = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel3
)


# cv2.imshow("Threshold", thresh)
cv2.imshow("Opening1", opening1)
cv2.imshow("Opening2", opening2)
cv2.imshow("Opening3", opening3)

cv2.waitKey(0)
cv2.destroyAllWindows()