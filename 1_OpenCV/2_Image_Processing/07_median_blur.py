# Gaussian Blur is good for general smoothing, but Median Blur is especially useful for removing 
# small noise, such as:

# White dots on a dark background
# Black dots on a bright background
import cv2

img = cv2.imread("cat.jpg")

# Apply Median Blur
median = cv2.medianBlur(
    img,
    5
)

cv2.imshow("Original", img)
cv2.imshow("Median Blur", median)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Gaussian Blur
# cv2.GaussianBlur(img, (5, 5), 0)
# A 5 × 5 neighborhood

# and calculates a weighted average.

# Median Blur
# cv2.medianBlur(img, 5)

# Uses:

# A 5 × 5 neighborhood

# and selects the middle (median) pixel value.