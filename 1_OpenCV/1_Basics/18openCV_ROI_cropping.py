import cv2

img = cv2.imread("cat.jpg")

if img is None:
    print("Image not found!")
    exit()

print("Image Shape:", img.shape)

crop = img[20:330, 350:550]

cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()




# -------------------------
# Paste it somewhere else
# -------------------------
# img[20:330, 250:450] = crop

cv2.imshow("Modified Image", img)
