import cv2
import numpy as np

current_frame = None

# Will store the selected color range
lower = None
upper = None


def mouse(event, x, y, flags, param):
    global current_frame, lower, upper

    if event == cv2.EVENT_LBUTTONDOWN:

        hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        h, s, v = hsv[y, x]

        print(f"Clicked HSV : ({h}, {s}, {v})")

        lower = np.array([
            max(h - 10, 0),
            max(s - 50, 50),
            max(v - 50, 50)
        ])

        upper = np.array([
            min(h + 10, 179),
            min(s + 50, 255),
            min(v + 50, 255)
        ])

        print("Lower :", lower)
        print("Upper :", upper)


cap = cv2.VideoCapture(0)

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse)

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    current_frame = frame.copy()

    cv2.imshow("Webcam", frame)

    # Show mask only after a color is selected
    if lower is not None:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower, upper)

        cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




# Component	OpenCV Range
# Hue (H)	            0 to 179
# Saturation (S)	    0 to 255
# Value (V)	            0 to 255
