import cv2
# This tells what action occurred.(mouse)
# flags tells which buttons or modifier keys are currently active.
# This is your own custom data.
def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse Clicked")
        print("X =", x)
        print("Y =", y)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse)

while True:
    ret, frame = cap.read()

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
