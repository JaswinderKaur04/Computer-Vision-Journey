import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
# H = Hue (the actual color)
# S = Saturation (how pure the color is)
# V = Value (brightness)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("BGR Image", frame)
    cv2.imshow("HSV Image", hsv)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()