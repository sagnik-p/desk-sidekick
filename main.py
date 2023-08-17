import queries
import speak
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print(queries.getGPTAnswer("define avalanche breakdown","explain"))
engine.runAndWait()