

import sounddevice as sd
import librosa
import numpy as np
from scipy.io.wavfile import write
import pandas as pd


  # get the first vector


def record_audio():
    fs = 44100
    duration = 3

    print("how many recordings?? ")
    n = int(input())

    for i in range(0, n+1):
        print("recording started")

        rec = sd.rec(int((duration * fs)), samplerate=fs, channels=1)

        sd.wait()

        print("recording stopped")

        fileName = "data\new" + ".wav"
        write(filename=fileName, rate=fs, data=rec)

        print("record again ?\n1 for yes and 0 for no")
        choice = int(input())
        if choice == 1:
            continue
            
        else:
            break


#used in model.py




# def extract_mfcc(file, n_mfcc=40):
#     audio, sr = librosa.load(file)

#     mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc).T, axis=0)

#     return mfccs
def extract_mfcc(file, n_mfcc):
    signal, sr = librosa.load(file, sr=None)
    mfccs = np.mean(librosa.feature.mfcc(signal, sr=sr, n_mfcc=n_mfcc).T, axis=0)
    return mfccs

# df = pd.DataFrame(columns=range(0,40))
# print(df.columns)
# for i in range(0, 21):
#     fileName = "audio/" + str(i) + ".wav"

#     mfccs = extract_mfcc(fileName, 40)
#     lst = list(mfccs)
#     df.loc[len(df)] = lst

# print(df)
# df.to_csv("data/csv/n.csv") 





# df1 = pd.read_csv("data\complete_data.csv")
# print(df1.shape)
# df2 = pd.read_csv("data\priansh.csv")
# print(df2.shape)
# df1 = df1.append(df2, ignore_index=True)
# print(len(df1))
# df1.to_csv("data\complete_data.csv")



# record_audio()
