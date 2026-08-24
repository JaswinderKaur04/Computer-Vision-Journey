import cv2
import matplotlib.pyplot as plt

# Read color image
img = cv2.imread("cat.jpg")

# Calculate histograms for B, G, R
blue_hist = cv2.calcHist([img], [0], None, [256], [0, 256]) 
green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
red_hist = cv2.calcHist([img], [2], None, [256], [100, 200]) #Intensity = amount/value of red

# Display
plt.plot(blue_hist, label="Blue",color="blue")
plt.plot(green_hist, label="Green",color="green")
plt.plot(red_hist, label="Red",color="red")

plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.legend()

plt.show()

# The label= gives a name to each plot, and:

# plt.legend()

# displays those names on the graph.