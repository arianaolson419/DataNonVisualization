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
from aupyom import Sampler, Sound # Audio manipulation library
import math

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

def bin_data(y, num_bins, std_away):
    """Places indices of data points into bins to play discrete sounds
    Parameters
    ----------
    y : the y axis coordinates of the data
    num_bins : the number of bins above the mean that the data is separated into (in addition
    to two outlier bins.
    std_away : the width of the bins

    Returns
    -------
    a numpy array of signed integers representing pitch shifts
    """
    mean = np.mean(y)
    std = np.std(y)
    pitch_shifts = np.arange(-num_bins, num_bins + 1)
    thresholds = (std * std_away) * pitch_shifts + mean

    result = []
    for point in y:
        if point < thresholds[0]:
            result.append(pitch_shifts[0] - 1)
        elif point > thresholds[-1]:
            result.append(pitch_shifts[-1] + 1)
        else:
            for i in range(len(thresholds) - 1):
                if point >= thresholds[i] and point < thresholds[i + 1]:
                    result.append(i - num_bins)
    return np.array(result)

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

def play_from_point(sound, pitch_shifts, speed, stop_bool, x_coord=0):
    """Plays the tone pitchshifted coresponding to a starting point in the data
    Parameters
    ----------
    sound : the aupyom sound being played
    pitch_shifts : an array of the pitch shifts corresponding to the data
    speed : the number of data points per second to be played
    x_coord : the starting x_coordinate at which to play the sound
    """
    while stop_bool == False:
        for pitch in pitch_shifts[0:]:
            sound.pitch_shift = pitch
            print(pitch)
            time.sleep(1 / speed)
    else:
        pass

def FastForward():
    #This function will let you move forward in the dataset, I'm hoping
    pass

def Rewind():
    #This function will let you move backwards in the dataset, I'm hoping
    pass


if __name__ == "__main__":
                    # 0 : up
                    # 1 : right
                    # 2 : down
                    # 3 : left
    filepath = "mvp.csv"
    fs = 44100
    x, y = get_csv_data(filepath)
    slopes = find_slopes(x, y)
    randvar = np.random.normal(0, 1, 100)
    binned = bin_data(y, 10, .5)
    pitch_shifts = binned
    speed = 5
    sampler = Sampler()
    s1 = Sound.from_file("A.wav")
    xpoint = 0
    paused = False
    key = keyhit.KBHit()
    while True:
        print("arrow")
        if paused == False:
            arrow = key.getarrow()
            print("STARTING SAMPLER")
            while (paused == False):
                print("while paused is false")
                sampler.play(s1)
                since_start = time.clock()
                for pitch in pitch_shifts[0:]:
                    pausearrow = key.getarrow()
                    if pausearrow == arrow:
                        s1.pitch_shift = pitch
                    #print(pitch)
                        time.sleep(1 / speed)

                    elif (pausearrow == 2):
                        print("PAUSE")
                        paused = True
                    #stop_bool = True
                        pause_time = time.clock()
                        xpoint = xpoint + math.ceil((pause_time-since_start)/speed)
                        print(xpoint)
                        s1.playing = False
                        break
                    else:
                        pass

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


    filepath = "mvp.csv"
    fs = 44100
    x, y = get_csv_data(filepath)
    slopes = find_slopes(x, y)
