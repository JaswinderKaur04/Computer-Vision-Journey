import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(img, (400, 400), (400, 500), (0, 255, 0), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()







# import numpy as np

# img = np.full((300, 300, 3), (0, 255, 255), dtype=np.uint8)



# img = np.zeros((300, 300, 3), dtype=np.uint8)
# img[:] = (0, 255, 255)

# Here, [:] means take the entire list.
# Select the entire image.

# img[0] = (0,255,255)
# img[:, 0] = (255, 0, 0)
# img[100:200, 100:200] = (0, 255, 0)