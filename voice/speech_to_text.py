
import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    return r.recognize_google(audio)
