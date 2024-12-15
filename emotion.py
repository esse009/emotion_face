import cv2
from deepface import DeepFace
from picamera2 import Picamera2

# Load face cascade classifier

def get_camera():
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"format": 'RGB888',
                                                            "size": (1920, 1080)}))
    picam2.start()
    return picam2

def cleanup_camera(camera):
    camera.stop()

def get_classifier():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def get_emotion(camera, classifier):
    frame = camera.capture_array()
    faces = classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if (len(faces) == 0):
        return "neutral"
    # We only analyse one face or we would get confused
    (x, y, w, h) = faces[0]
    # Extract the face ROI (Region of Interest)
    face_roi = frame[y:y + h, x:x + w]

    # Perform emotion analysis on the face ROI
    result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

    # Determine the dominant emotion
    emotion = result[0]['dominant_emotion']
    print(emotion)
    return emotion


