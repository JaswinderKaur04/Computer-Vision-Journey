import cv2

img = cv2.imread("cat.jpg")

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("90 Clockwise", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()