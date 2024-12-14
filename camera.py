from picamera2 import Picamera2
from time import sleep
import io
from PIL import Image




key = "4DiqYo3wSQg7iHb5Kxn7LCG2IYgbUWMn1Vk53f1Fcc4V7o799kLzJQQJ99ALACi5YpzXJ3w3AAAEACOGOWKs"

picam2 = Picamera2()
picam2.start()

def get_image() -> bytes:
  # BytesIO is a file-like buffer stored in memory
  imgByteArr = io.BytesIO()
  # image.save expects a file-like as a argument
  picam2.capture_file(imgByteArr, format="png")
  # Turn the BytesIO object back into a bytes object
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr



with FaceClient(endpoint=endpoint, credential=AzureKeyCredential(key)) as face_client:
    image = picam2.capture_image()
    result = face_client.detect(get_image(),
        return_face_id=False,
        detection_model=FaceDetectionModel.DETECTION03,
        recognition_model=FaceRecognitionModel.RECOGNITION04,
        return_face_landmarks=True
    )
    print(result)


picam2.stop()
