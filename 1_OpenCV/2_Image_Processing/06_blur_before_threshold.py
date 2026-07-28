# real images may contain small unwanted variations/noise.

#         Image
#           ↓
#         Blur
#           ↓
#     Small variations are reduced
#           ↓
#        Threshold
#           ↓
#       Cleaner result

# Gaussian Blur = Preprocessing
# Thresholding  = Segmentation 

import cv2

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)

# Apply thresholding
_, threshold = cv2.threshold(
    blur,
    127,
    255,
    cv2.THRESH_BINARY
)

# Display results
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()