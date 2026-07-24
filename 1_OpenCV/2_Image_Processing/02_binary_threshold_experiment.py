import cv2

# Read image
img = cv2.imread("cat.jpg")

# Convert BGR image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
threshold_value, binary_image = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Display result
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Binary Threshold", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()