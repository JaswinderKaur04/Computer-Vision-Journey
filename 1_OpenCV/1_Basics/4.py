import cv2
import os

# -------------------------------
# Load Haar Cascade Classifiers
# -------------------------------
face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
eye_path = cv2.data.haarcascades + "haarcascade_eye.xml"

# Check if XML files exist
if not os.path.exists(face_path):
    print("Face cascade XML file not found:")
    print(face_path)
    exit()

if not os.path.exists(eye_path):
    print("Eye cascade XML file not found:")
    print(eye_path)
    exit()

face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

# Check if cascade files loaded correctly
if face_cascade.empty():
    print("Face cascade not loaded properly")
    exit()

if eye_cascade.empty():
    print("Eye cascade not loaded properly")
    exit()

print("Cascade files loaded successfully")

# -------------------------------
# Start Webcam
# -------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not opened")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# -------------------------------
# Main Loop
# -------------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Show face count on screen
    face_count = len(faces)
    cv2.putText(
        frame,
        f"Faces Detected: {face_count}",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    # Detect eyes inside each detected face
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            3
        )

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(15, 15)
        )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

    # Display output
    cv2.imshow("Face and Eye Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -------------------------------
# Release Resources
# -------------------------------
cap.release()
cv2.destroyAllWindows()