import cv2

img = cv2.imread("cat.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
cv2.imshow("ORIGINAL image window",img)
cv2.imshow("GRAY SCALE image window",gray)
cv2.waitKey(0)