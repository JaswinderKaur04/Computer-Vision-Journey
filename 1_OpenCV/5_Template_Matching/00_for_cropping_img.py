import cv2 

img = cv2.imread("original_img.jpg")


img = img[131:453,104:298]
cv2.imshow("image",img)
cv2.waitKey(0)
img = cv2.imwrite("cropped_img.jpg",img)
