# Contours
# A contour is the boundary or outline of an object.
# These connected lines together form one shape/object.
import cv2

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Find contours
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours
cv2.drawContours(
    img,
    contours,
    -1,
    (0, 255, 0),
    2
)
# print(len(contours))
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()