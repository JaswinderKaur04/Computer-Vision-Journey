import cv2
import numpy as np

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find minimum and maximum intensity
min_val = np.min(gray)
max_val = np.max(gray)

# Contrast stretching
stretched = ((gray - min_val) / (max_val - min_val)) * 255

# Convert to uint8
stretched = stretched.astype(np.uint8)

# Display
cv2.imshow("Original", gray)
cv2.imshow("Contrast Stretched", stretched)

print("Original min:", min_val)
print("Original max:", max_val)

print("Stretched min:", stretched.min())
print("Stretched max:", stretched.max())

cv2.waitKey(0)
cv2.destroyAllWindows()