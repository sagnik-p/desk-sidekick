import pyttsx3
from gtts import gTTS
from playsound import playsound
# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
playsound("welcome.mp3")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
def say(txt):
    engine.say(txt)
    engine.runAndWait()