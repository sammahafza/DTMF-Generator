# Created by Samer Mahafza
import numpy as np
import sounddevice as sd
import time

low_freq = [697, 770, 852, 941]
high_freq = [1209, 1336, 1477, 1633]

# "digit": [low_freq, high_freq]
digits_tones = \
{ "1": [0, 0],
  "2": [0, 1],
  "3": [0, 2],
  "A": [0, 3],
  "4": [1, 0],
  "5": [1, 1],
  "6": [1, 2],
  "B": [1, 3],
  "7": [2, 0],
  "8": [2, 1],
  "9": [2, 2],
  "C": [2, 3],
  "*": [3, 0],
  "0": [3, 1],
  "#": [3, 2],
  "D": [3, 3]
}

valid_digits = "0123456789*#ABCD"

duration = 0.5
volume = 0.5
fs = 44100 # sampling rate


while True:
    digits = list(input("Enter the digits: ").replace(" ",""))
    if(all(d in valid_digits for d in digits)):
        for i in digits:
            f1 = low_freq[digits_tones[i][0]]
            f2 = high_freq[digits_tones[i][1]]
            s1 = np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)
            s2 = np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)

            sd.play(s1*volume + s2*volume)
            time.sleep(1)
    else:
        print("wrong input..")
