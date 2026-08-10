import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate histogram
hist = cv2.calcHist(
    [gray],
    [0],     #For our grayscale image, there is only one channel, so its index is 0
    None,    #Calculate the histogram using the entire image
    [16],   #Think of bins as boxes used to count pixels.Create 256 boxes, one for each intensity value.
    [0, 256] #0 ─────────────── 255
             #Black             White

             #That's why we normally write:[0, 256]because OpenCV's upper limit is exclusive → actual values are 0–255.
)
cv2.imshow("original",gray)
cv2.waitKey(0)
# Display histogram
plt.plot(hist)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.show()



cv2.destroyAllWindows()

# With 16 bins, intensities are grouped together:

# 0–15    → Bin 1
# 16–31   → Bin 2
# 32–47   → Bin 3
# ...
# 240–255 → Bin 16