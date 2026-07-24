import cv2

img = cv2.imread("cat.jpg")

flip = cv2.flip(img, -1)

cv2.imshow("Original", img)
cv2.imshow("Both Flip", flip)

cv2.waitKey(0)
cv2.destroyAllWindows()