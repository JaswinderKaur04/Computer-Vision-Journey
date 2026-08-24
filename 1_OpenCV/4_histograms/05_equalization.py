# Suppose an image has most of its pixels squeezed into a small intensity range:

# 0 ──────────────── 255
#        ███████
#        pixels

# The image may look low contrast / dull.

# Histogram Equalization tries to spread those intensities across a wider range:

# 0 █████████████████████████████████████ 255

# Result → better contrast.

import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized = cv2.equalizeHist(gray)

# -------------------------------
# Display images
# -------------------------------

cv2.imshow("Original Grayscale", gray)
cv2.imshow("Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()


# -------------------------------
# Display Original Histogram
# -------------------------------

plt.hist(gray.ravel(), 256, [0, 256])
plt.title("Original Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()


# -------------------------------
# Display Equalized Histogram
# -------------------------------

plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("Equalized Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()

# An image is normally 2D:

# Image:
# [
#  [10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]
# ]

# .ravel() changes it to:

# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Why do we need it for the histogram?

# plt.hist() needs the pixel values as a collection of values to count.




# OpenCV's calcHist() is specifically designed to receive an image array, including a 2D grayscale image.

# You give it:

# gray
#   ↓
# 2D image
#   ↓
# cv2.calcHist()
#   ↓
# counts pixels automatically
#   ↓
# histogram

# So OpenCV handles the pixels internally. You don't need to convert the image to 1D.

# 2. plt.hist() works differently

# When you write:

# plt.hist(equalized.ravel(), 256, [0, 256])

# plt.hist() is a general-purpose data histogram function. We give it the pixel values as data.

# Therefore, we commonly convert:

# 2D image
#      ↓
# ravel()
#      ↓
# 1D pixel values
#      ↓
# plt.hist()