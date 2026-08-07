import cv2
import numpy as np

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(thresh, kernel, iterations=2)  #Apply erosion once.

# Display
# cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()




# kernel = np.ones((5,5), np.uint8)
# kernel = np.ones((3,3), np.uint8)
# kernel = np.ones((7,7), np.uint8)
# iterations = 2