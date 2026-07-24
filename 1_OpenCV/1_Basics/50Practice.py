import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("orignal window",frame)
    cv2.imshow("HSV window",hsv_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()    
cv2.destroyAllWindows()
    