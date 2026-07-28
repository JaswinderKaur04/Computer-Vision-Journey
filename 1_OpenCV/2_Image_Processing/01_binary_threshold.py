# A threshold is a cutoff point or boundary used to make a decision.
# We use thresholding in image processing to separate important objects from the background. 
# Pixel > threshold → 255 (white)
# Pixel ≤ threshold → 0 (black)
import cv2

img = cv2.imread("cat.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(
    gray,
    200,       #if pixel>200
    255,       #output
    cv2.THRESH_BINARY
)

# cv2.imshow("Original", img)
# cv2.imshow("Gray", gray)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()


# if pixel > 127:
#     output = 255  # white
# else:
#     output = 0    # black

# 0 ─────────────── 127 ─────────────── 255
    #  BLACK              WHITE
    
    
# In Python, _ is commonly used as a variable name when:
# We receive a value, but we don't need to use it.   



# _, threshold
# threshold_value, threshold_image 
# First output: threshold value. Second output: the complete processed threshold image.