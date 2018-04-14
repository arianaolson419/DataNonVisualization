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

    
def speedx(sound_array, factor):
    """ Multiplies the sound's speed by some `factor` """
    indices = np.round( np.arange(0, len(sound_array), factor) )
    indices = indices[indices < len(sound_array)].astype(int)
    return sound_array[ indices.astype(int) ]

def stretch(sound_array, f, window_size, h):
    """ Stretches the sound by a factor `f` """

    phase  = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros( (len(sound_array) /f + window_size), dtype=np.int32)

    for i in np.arange(0, len(sound_array)-(window_size+h), h*f):

        # two potentially overlapping subarrays
        a1 = sound_array[i: i + window_size]
        a2 = sound_array[i + h: i + window_size + h]

        # resynchronize the second array on the first
        s1 =  np.fft.fft(hanning_window * a1)
        s2 =  np.fft.fft(hanning_window * a2)
        phase = (phase + np.angle(s2/s1)) % 2*np.pi
        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))

        # add to result
        i2 = int(i/f)
        result[i2 : i2 + window_size] += hanning_window*a2_rephased

    result = ((2**(16-4)) * result/result.max()) # normalize (16bit)

    return result.astype('int16')

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

    fast = speedx(de[:re], 1.5)
    slow = speedx(de[:re], 0.75)
    #fast = stretch(de[:re], 1, 1, 1)
    #slow = stretch(de[:re], 2, 1, 1)
    for i in range(len(x)-1):
        if slopes[i]>0:
            sd.play(slow, re, blocking=True)
            print("positive")
        elif slopes[i] == 0:
            sd.play(dc[:re], re, blocking=True)
            #sd.play(c_array, fs)
            print('zero')
        elif slopes[i] < 0:
            sd.play(fast, re, blocking=True)
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
