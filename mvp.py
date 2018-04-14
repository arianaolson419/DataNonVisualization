"""The MVP: Play a different tone for positive and negative slopes.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import wavfile
import sounddevice as sd

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

def make_sounds(slopeChange):
    """Plays a tone wavefile based on up, same, or down input
    ----------
    slopeChange : up, same, or down input in slope 

    Returns
    -------
    Nothing, plays wavfile
    """
    slopes = np.zeros((len(x) - 1))
    for i in range(len(x) - 1):
        # m = (y2 - y1) / (x2 - x1)
        delta_x = x[i + 1] - x[i]
        delta_y = y[i + 1] - y[i]
        slopes[i] = delta_y / delta_x 
    return slopes

if __name__ == "__main__":
    filepath = "mvp.csv"
    x, y = get_csv_data(filepath)
    slopes = find_slopes(x, y)
    # Plot the slopes to verify they are correct
    plt.plot(slopes)
    plt.show()
