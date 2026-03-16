# 🧠 Neuro-Therap / TherapIA

Asistente psicológico con inteligencia artificial basado en terapia cognitivo-conductual (TCC), detección de emociones y apoyo emocional en tiempo real.

---

## 📁 Estructura del proyecto

```
neuro_therap/
│
├── main.py                  # Servidor FastAPI (punto de entrada)
├── config.py                # Configuración y variables de entorno
├── requirements.txt         # Dependencias
├── .env.example             # Plantilla de variables de entorno
├── .gitignore
│
├── ai_core/                 # Núcleo de inteligencia artificial
│   ├── emotion_detector.py  # Detección de emociones en texto y cámara
│   ├── response_generator.py# Generación de respuestas con GPT
│   └── cbt.py               # Módulo de terapia cognitivo-conductual
│
├── monitoring/              # Seguridad y control
│   ├── emergency_protocol.py# Detección de crisis
│   ├── time_restrictions.py # Restricciones de horario
│   └── usage_control.py     # Control de uso diario
│
├── voice/                   # Módulos de voz
│   ├── speech_to_text.py    # Reconocimiento de voz
│   └── text_to_speech.py    # Síntesis de voz
│
├── utils/                   # Utilidades generales
│   └── quotes.py            # Frases motivacionales
│
└── frontend/
    └── index.html           # Interfaz web del chat
```

---

## ⚙️ Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/neuro-therap.git
cd neuro-therap

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Edita .env y agrega tu API key de OpenAI

# 5. Ejecutar
uvicorn main:app --reload
```

---

## 🔐 Variables de entorno

Crea un archivo `.env` basado en `.env.example`:

```
OPENAI_API_KEY=tu_api_key_aqui
MAX_DAILY_HOURS=3
```

> ⚠️ **Nunca subas tu archivo `.env` a GitHub.**

---

## 🚀 Funcionalidades

- 💬 Chat terapéutico con IA (GPT-4o-mini)
- 🎭 Detección de emociones en texto
- 🚨 Protocolo de emergencia ante crisis
- 🎤 Entrada y salida de voz
- 🫁 Ejercicios de respiración
- 🧠 Técnicas CBT (terapia cognitivo-conductual)
- 📓 Journaling guiado
- ⏰ Control de horario y uso diario

---

## 🛠️ Tecnologías

- Python 3.13
- FastAPI + Uvicorn
- OpenAI GPT-4o-mini
- HuggingFace Transformers
- OpenCV + MediaPipe
- SpeechRecognition + pyttsx3
