# Closing is also a combination of two operations, but the order is reversed.
# Opening = Erosion → Dilation
# Closing = Dilation → Erosion


import cv2
import numpy as np

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Closing
closing = cv2.morphologyEx(
    thresh,
    cv2.MORPH_CLOSE,
    kernel
)
# Opening removes small white noise. It does not expand the white dots.
opening = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel
)

# Display
cv2.imshow("Threshold", thresh)
cv2.imshow("Closing", closing)
cv2.imshow("opening", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()