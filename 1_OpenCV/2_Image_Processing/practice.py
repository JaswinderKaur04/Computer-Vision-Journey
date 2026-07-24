import cv2

img = cv2.imread("cat.jpg")

_,thres = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY
)

_,thres_inv = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY_INV
)

cv2.imshow("image with threshold",thres)
cv2.imshow("image with threshold inverse",thres_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()