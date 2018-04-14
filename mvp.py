"""The MVP: Play a different tone for positive and negative slopes.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sounddevice as sd
from scipy.io import wavfile
import sys
import msvcrt, time
import keyhit as keyhit #thanks Washington and Lee university

def change_music(wav):
    fs, musicdata = wavfile.read(wav); #save the sampling frequency and the numpy array of frequency numbers
    return musicdata

def get_csv_data(filepath):
    """Extract x and y values from a csv file.
    Parameters
    ----------
    filepath : the path to the file

    Returns
    -------
    x : the x coordinates
    y : the y coordinates
    """
    # Read the csv file into a pands dataframe
    csv_df = pd.read_csv(filepath)

    # Read the columns into coordinate arrays
    x = csv_df.iloc[:, 0]
    y = csv_df.iloc[:, 1]
    return x, y

def find_slopes(x, y):
    """finds the slopes between each point in the data
    Parameters
    ----------
    x : the x coordinates of the data.
    y : the y coordinates of the data

    Returns
    -------
    slopes : a numpy array with each element being the slope between
    consecutive points.
    """
    slopes = np.zeros((len(x) - 1))
    for i in range(len(x) - 1):
        # m = (y2 - y1) / (x2 - x1)
        delta_x = x[i + 1] - x[i]
        delta_y = y[i + 1] - y[i]
        slopes[i] = delta_y / delta_x
    return slopes

def play_slope(slopes,fs):
    # """Plays a tone wavefile based on up, same, or down input
    # A = negative tone
    # E = Positive Atone
    # C = no change
    # ----------
    # slopeChange : up, same, or down input in slope
    # Returns
    # -------
    # Nothing, plays wavfile""

    for i in range(len(x)-1):
        if slopes[i]>0:
            sd.play(de[:re], re, blocking=True)
            print("positive")
        elif slopes[i] == 0:
            sd.play(dc[:rc], rc, blocking=True)
            #sd.play(c_array, fs)
            print('zero')
        elif slopes[i] < 0:
            sd.play(da[:ra], ra, blocking=True)
            #sd.play(a_array, fs)
            print('negative')
        else:
            print("Not a slope?")

                # if slopeChange > 0:
                #     r, d = wavfile.read("E.wav")
                # elif slopeChange < 0:
                #     r, d = wavfile.read("A.wav")
                # else:
                #     r, d = wavfile.read("C.wav")
                # sd.play(d, r, blocking=True)

def FastForward():
    #This function will let you move forward in the dataset, I'm hoping
    pass

def Rewind():
    #This function will let you move backwards in the dataset, I'm hoping
    pass


if __name__ == "__main__":
    paused = False
    key = keyhit.KBHit()
    while True:
        if paused == False:
            while (paused == False):
                pausearrow = key.getarrow()
                # 0 : up
                # 1 : right
                # 2 : down
                # 3 : left
                if pausearrow== 2:
                    print("PAUSE")
                    paused = True
                    break
                time.sleep(0.1)
        if paused == True:
            playarrow = key.getarrow()
            while paused:
                if playarrow == 0:
                    #hit up to play again
                    print ("PLAY")
                    paused = False
                    break
                elif playarrow == 1:
                    #hit right to go forward in the data
                    print("Fast Forward")
                    FastForward()
                    break
                elif playarrow == 3:
                    #hit left to go backwards in the data
                    print("Rewind")
                    Rewind()
                    break
                elif playarrow == 2:
                    #if you hit pause again, then unpause
                    print ("PLAY")
                    paused = False
                    break
                print(" .. ")
                time.sleep(0.1)
        else:
            print(" . ")
