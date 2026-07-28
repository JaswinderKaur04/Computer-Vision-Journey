# It smooths the image while trying to preserve important edges.

# img

# The original image.

# 9

# The neighborhood diameter:

# 9 → considers a larger nearby area
# First 75

# Controls how much color/intensity difference is considered.

# Second 75

# Controls the spatial distance between pixels.

# For now, you don't need to memorize the mathematical details.

import cv2

img = cv2.imread("cat.jpg")

# Apply Bilateral Filter
bilateral = cv2.bilateralFilter(
    img,
    9,
    75,
    75
)

cv2.imshow("Original", img)
cv2.imshow("Bilateral Filter", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()