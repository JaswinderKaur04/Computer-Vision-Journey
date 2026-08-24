import cv2 
img = cv2.imread("multiple_images_in_one_img.jpg")
img = img[112:163,14:80]

cv2.imwrite("cropped_image_from_multiple_img.jpg",img)