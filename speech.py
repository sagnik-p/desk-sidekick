import pyttsx3
from gtts import gTTS
from playsound import playsound
# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio


# Language in which you want to convert
language = 'en'
myobj = gTTS(text="sure sir, here is what I found", lang=language, slow=False)
myobj.save("reply.mp3")
playsound("reply.mp3")
os.remove("reply.mp3")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
def say(txt):
    engine.say(txt)
    engine.runAndWait()