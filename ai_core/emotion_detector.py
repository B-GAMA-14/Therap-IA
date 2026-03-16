from transformers import pipeline
import cv2

# Modelo de detección de emociones en texto
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def detect_emotion(text):

    try:
        result = emotion_model(text)[0][0]
        return result["label"]
    except:
        return "neutral"


def detect_face_emotion():

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        return "No se pudo acceder a la cámara"

    ret, frame = cam.read()

    cam.release()

    if not ret:
        return "No se pudo capturar imagen"

    # Aquí podríamos poner un modelo real
    # por ahora solo simulamos

    return "neutral"