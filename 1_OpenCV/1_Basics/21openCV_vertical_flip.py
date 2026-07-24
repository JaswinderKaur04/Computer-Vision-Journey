import cv2

img = cv2.imread("cat.jpg")

flip = cv2.flip(img, 0)

cv2.imshow("Original", img)
cv2.imshow("Vertical Flip", flip)

cv2.waitKey(0)
cv2.destroyAllWindows()