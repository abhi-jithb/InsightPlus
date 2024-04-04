from django.conf import settings
from PyEmotion import DetectFace
import cv2 as cv

class ImageExpressionDetect:
    def getExpression(self, imagepath):
        filepath = settings.MEDIA_ROOT + "/" + imagepath  # Use "/" instead of "\\"
        er = DetectFace(device='cpu', gpu_id=0)
        frame, emotion = er.predict_emotion(cv.imread(filepath))
        cv.imshow('InsightPlus', frame)
        cv.waitKey(0)
        print("Hi", filepath, "Emotion is", emotion)
        return emotion

    def getLiveDetect(self):
        print("Streaming Started")
        er = DetectFace(device='cpu', gpu_id=0)
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Failed to open camera")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                continue

            frame, emotion = er.predict_emotion(frame)
            cv.imshow('Press Q to Exit', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()
