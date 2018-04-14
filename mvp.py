"""The MVP: Play a different tone for positive and negative slopes.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sounddevice as sd
from scipy.io import wavfile

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

def play_slope(slopes, a_array, e_array, c_array, fs):
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
            sd.play(e_array, fs)
            print("positive")
        elif slopes[i] == 0:
            sd.play(c_array, fs)
            print('zero')
        elif slopes[i] < 0:
            sd.play(a_array, fs)
            print('negative')
        else:
            print("Not a slope?")

if __name__ == "__main__":
    filepath = "mvp.csv"
    fs = 44100
    x, y = get_csv_data(filepath)
    slopes = find_slopes(x, y)
    # Plot the slopes to verify they are correct
    plt.plot(slopes)
    plt.show()
    a_array = change_music('Atone.wav')
    e_array = change_music('Etone.wav')
    c_array = change_music('Ctone.wav')
    play_slope(slopes, a_array, e_array, c_array, fs)
