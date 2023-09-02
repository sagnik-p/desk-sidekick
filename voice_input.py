import speech_recognition as sr
import string
r=sr.Recognizer()
mic = sr.Microphone()
def listen_and_recognize():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return r.recognize_google(audio).lower()
