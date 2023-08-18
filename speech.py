import pyttsx3
from gtts import gTTS
import socket
from playsound import playsound
import os
language = 'en'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
def sayOfffline(txt):
    engine.say(txt)
    engine.runAndWait()

def sayOnline(txt):
    myobj = gTTS(text=txt, lang=language,tld="us", slow=False)
    myobj.save("reply.mp3")
    playsound("reply.mp3")
    os.remove("reply.mp3")

def say(txt):
    if(isOnline()):
        sayOnline(txt)
    else:
        sayOfffline(txt)

def isOnline():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        pass
    return False