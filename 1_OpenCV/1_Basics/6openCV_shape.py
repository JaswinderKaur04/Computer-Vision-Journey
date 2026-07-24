import cv2

img = cv2.imread("cat.jpg")

print("Shape :", img.shape)
print("Height:", img.shape[0])
print("Width :", img.shape[1])
print("Channels:", img.shape[2])