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