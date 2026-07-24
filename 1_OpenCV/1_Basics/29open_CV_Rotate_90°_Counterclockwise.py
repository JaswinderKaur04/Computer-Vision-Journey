import cv2

img = cv2.imread("cat.jpg")

rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("90 Counter Clockwise", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Original:
# Height = 350
# Width = 700
# Rotated:
# Height = 700
# Width = 350

# The height and width swap because the image has been rotated by 90°.