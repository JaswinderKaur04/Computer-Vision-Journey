# pip install opencv-python
import cv2
import time
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)   # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Height

while True:
    ret, frame = cap.read()   # frame 1 photo in stream of photos in video
    cv2.imshow('bcet feed', frame)
    print("press q to exit")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()