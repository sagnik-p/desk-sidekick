###### IMPORTS ###################
import os
import threading
import time
import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model

listeningThreadRunning=False
PredictionThreadRunning=False
##### CONSTANTS ################
fs = 44100
seconds = 2

model = load_model(os.getcwd() + "/WakeWord\saved_model\WWD.h5")


##### LISTENING THREAD #########
def listener():
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        prediction_thread(mfcc_processed)
        time.sleep(1)


def listenForWW():
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listeningThreadRunning=True
    listen_thread.start()

def stopListeningForWW():
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listeningThreadRunning=False
    listen_thread.st()

##### PREDICTION THREAD #############
def prediction(y):
    prediction = model.predict(np.expand_dims(y, axis=0))
    if prediction[:, 1] > 0.99:
        print("wakeword detected with confidence : ",end='')
        print(prediction[:,1])
        return True
    return False



def prediction_thread(y):
    pred_thread = threading.Thread(target=prediction, name="PredictFunction", args=(y,))
    pred_thread.start()


listenForWW()
