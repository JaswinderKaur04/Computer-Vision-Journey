import cv2
import numpy as np

img = np.zeros((500,500,3), dtype=np.uint8)

# Line
cv2.line(img, (50,50), (450,50), (255,0,0), 2)

# Rectangle
cv2.rectangle(img, (50,100), (200,250), (0,255,0), 2)

# Circle
cv2.circle(img, (350,180), 70, (0,0,255), -1)

# Text
cv2.putText(img, "OpenCV", (140,420),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (255,255,255),
            2)

cv2.imshow("Shapes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()