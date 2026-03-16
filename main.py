from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from ai_core.response_generator import generate_response
from monitoring.usage_control import check_usage
from monitoring.time_restrictions import is_allowed_time
from monitoring.emergency_protocol import evaluate_risk
from ai_core.emotion_detector import detect_emotion, detect_face_emotion

app = FastAPI(title="Neuro-Therap API")

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# ---------- MODELOS ----------

class ChatRequest(BaseModel):
    user_id: str = "usuario_demo"
    message: str


class EmotionRequest(BaseModel):
    text: str


# ---------- RUTAS ----------

@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/chat")
async def chat(data: ChatRequest):

    user_id = data.user_id
    message = data.message

    # Restricción de horario
    if not is_allowed_time():
        return {"response": "Modo nocturno activo 🌙 Estoy contigo."}

    # Control de uso
    if not check_usage(user_id):
        return {
            "response": "Hemos trabajado mucho hoy en tus emociones. Ahora te invito a que pongas en práctica lo que hablamos en el mundo real. ¡Vuelve mañana!"
        }

    # Evaluación de riesgo emocional
    risk = evaluate_risk(message)

    if risk == "critical":
        return {
            "response": "Detecto señales importantes en lo que dices. Te recomiendo buscar ayuda profesional o hablar con alguien de confianza 💛"
        }

    # Generar respuesta de la IA
    response = generate_response(user_id, message)

    return {
        "response": response
    }


@app.post("/emotion")
async def emotion(data: EmotionRequest):

    detected = detect_emotion(data.text)

    return {
        "emotion": detected
    }


@app.get("/face")
async def face():

    detected = detect_face_emotion()

    return {
        "emotion": detected
    }
