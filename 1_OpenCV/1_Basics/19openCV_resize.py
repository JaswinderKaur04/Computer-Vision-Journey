import cv2
img = cv2.imread("cat.jpg")

resized = cv2.resize(img, (700, 300)) # width,height

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()