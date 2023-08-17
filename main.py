import queries
import speak
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say(queries.getDaVinviAnswer("define avalanche breakdown"))
engine.runAndWait()