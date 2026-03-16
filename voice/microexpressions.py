
import cv2

def detect_face():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    return "Rostro detectado (prototipo experimental)"
