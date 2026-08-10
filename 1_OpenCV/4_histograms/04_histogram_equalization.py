import cv2

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized = cv2.equalizeHist(gray)

cv2.imshow("Original Histogram", gray)
cv2.imshow("Equalized Histogram", equalized)

print("Original min:", gray.min())
print("Original max:", gray.max())

print("Equalized min:", equalized.min())
print("Equalized max:", equalized.max())

cv2.waitKey(0)
cv2.destroyAllWindows()

