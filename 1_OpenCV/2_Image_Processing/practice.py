import cv2

img = cv2.imread("cat.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

threshold_value,threshold = cv2.threshold(
    gray,
    150,
    255,
    cv2.THRESH_BINARY
)

threshold_value,inv = cv2.threshold(
    gray,
    150,
    255,
    cv2.THRESH_BINARY_INV
)
threshold_value,trunc = cv2.threshold(
    gray,
    150,
    255,
    cv2.THRESH_TRUNC
)

print(threshold_value)
cv2.imshow("threhold image",threshold)
cv2.imshow("myimage",gray)
cv2.imshow("myimage inverse",inv)
cv2.imshow("myimage trunc",trunc)
cv2.waitKey(0)