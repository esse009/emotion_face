import cv2
from deepface import DeepFace
from picamera2 import Picamera2

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# cv2.startWindowThread()

# Start capturing video
picam2 = Picamera2()

picam2.configure(picam2.create_video_configuration(main={"format": 'RGB888',
                                                           "size": (640, 480)}))

picam2.start()
while True:
    # Capture frame-by-frame
    frame = picam2.capture_array()
    # Convert frame to grayscale
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Convert grayscale frame to RGB format
    # rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # # Detect faces in the frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = frame[y:y + h, x:x + w]

        
        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        print(emotion)

        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    # cv2.imshow('frame', frame)

    # Press 'q' to exit
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    # cv2.waitKey(1)

# Release the capture and close all windows
picam2.stop()
cv2.destroyAllWindows()

