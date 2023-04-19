from model_testing import verifyUser
import sounddevice as sd
from scipy.io.wavfile import write
from creatingData import extract_mfcc

import pandas as pd
from sklearn.neural_network import MLPClassifier

import time
import warnings
import pyttsx3

#setup voice engine of py text to speech
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speaker_identifier():    
    fs = 44100
    duration = 3
    print("speak hey jarvis when the recording starts")
    engine.say("Speak hey jarvis to authorize!")
    engine.runAndWait()

    time.sleep(0.1)
    print("recording started")

    rec = sd.rec(int((duration * fs)), samplerate=fs, channels=1)

    sd.wait()

    print("recording stopped")

    file = "data\\history\\new.wav"
    #this will save the audio of the last person tried to access the software,
    # will help later to identify the person
    write(filename=file, rate=fs, data=rec)

    mfcc = extract_mfcc(file, n_mfcc=40) #defined in creatingData.py

    input = pd.DataFrame(columns=range(0, 40))

    lst = list(mfcc)
    input.loc[len(input)] = lst

    df = pd.read_csv("data\\csv\\complete_data.csv")  # target variable is boolean : 1 means authorized, 0 means unknown

    Y = df["speaker"]
    X = df.drop(columns=["speaker", "Unnamed: 0"])

    classifier = MLPClassifier(solver='adam', alpha=0.001,
                               random_state=1, max_iter=500,
                               hidden_layer_sizes=100, activation="logistic")

    warnings.simplefilter("ignore")
    classifier.fit(X, Y)

    pred_mlp = classifier.predict(input)
    return pred_mlp[0]


    # random forest, average
    # warnings.simplefilter("ignore")
    # clf_forest = RandomForestClassifier(max_depth=100, random_state=1
    #                                     , n_estimators=75, criterion="entropy",
    #                                     max_features="auto")
    # clf_forest.fit(X, Y)
    # pred_rf = clf_forest.predict(input)
    # return pred_rf[0]



