import cv2

cap = cv2.VideoCapture(0)

# Video settings
fourcc = cv2.VideoWriter_fourcc(*'XVID')  #This line tells OpenCV which video codec (compression format) to use  eg. 'MJPG','X264','DIVX'
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

recording = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize to match VideoWriter size
    frame = cv2.resize(frame, (640, 480))

    # Save frame only if recording
    if recording:
        out.write(frame)

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)

    if key == ord('r'):
        recording = True
        print("Recording Started")

    elif key == ord('s'):
        recording = False
        print("Recording Stopped")

    elif key == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()