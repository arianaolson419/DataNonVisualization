"""This is an MVP
"""
import numpy as np
import pandas as pd
from scipy.io import wavfile
import sounddevice as sd

def get_csv_data():
    """Extract x and y values from a csv file.
    Parameters
    ----------
    filepath : the path to the file

    Returns
    -------
    x : the x coordinates
    y : the y coordinates
    """
    pass

def find_slopes():
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
    pass

def make_sounds(slopeChange):
    """Plays a tone wavefile based on up, same, or down input
    ----------
    slopeChange : up, same, or down input in slope 

    Returns
    -------
    Nothing, plays wavfile
    """
    if slopeChange > 0:
        r, d = wavfile.read("E.wav")
    elif slopeChange < 0:
        r, d = wavfile.read("A.wav")
    else:
        r, d = wavfile.read("C.wav")
    sd.play(d, r, blocking=True)

if __name__ == "__main__":
   make_sounds(1)