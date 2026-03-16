from openai import OpenAI
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(user_id, message):

    system_prompt = """
Eres Therap-IA, un asistente psicológico basado en principios de terapia cognitivo conductual,
escucha activa y apoyo emocional.

Tu objetivo es:
- escuchar al usuario
- responder con empatía
- hacer preguntas reflexivas
- ayudar al usuario a explorar sus emociones

Reglas:
- no hables como robot
- no respondas como IA técnica
- habla como un psicólogo humano
- respuestas de máximo 4-6 líneas
- mantén tono cálido y humano
"""

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],

        temperature=0.7
    )

    return response.choices[0].message.content