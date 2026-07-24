# Contrast controls the difference between dark and bright pixels
# alpha = Contrast
# beta = Brightness
# New Pixel = (Old Pixel × alpha) + beta
# Old Pixel = 80

# alpha = 2

# beta = 30

# New Pixel = 80 × 2 + 30 = 190

# import cv2

# img = cv2.imread("cat.jpg")

# bright = cv2.convertScaleAbs(img, alpha=1, beta=60)

# cv2.imshow("Original", img)
# cv2.imshow("Bright", bright)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# import cv2

# img = cv2.imread("cat.jpg")

# contrast = cv2.convertScaleAbs(img, alpha=2, beta=0)

# cv2.imshow("Original", img)
# cv2.imshow("High Contrast", contrast)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




import cv2

img = cv2.imread("cat.jpg")

result = cv2.convertScaleAbs(img, alpha=1.5, beta=40)

cv2.imshow("Original", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()



# cv2.convertScaleAbs(), all three channels are changed in the same way, so the image
# usually looks like the same scene—just brighter, darker, or with more/less contrast.