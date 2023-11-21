# Code written by Krystal Lan
# R&D Intern @ Apex Skating Inc.
# Summer 2023

# Purpose: Extract all indices at times where the player changes directions
# Specify the player's Motion Capture data file to use in the "path" variable

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def find_all_peaks(data, prominence, threshold, height=None): # use prominence to tell how high it has to be above previous peaks (prevent double peaks)
    peaks, _ = find_peaks(data, prominence=prominence, height=height, threshold=threshold)
    troughs, _ = find_peaks(-data, prominence=prominence, height=height, threshold=threshold)
    return peaks, troughs

def pivot_index_range(peak_index, fs=200):
    num_points = fs/2
    indices = np.array([int(peak_index-num_points), int(peak_index+num_points)])
    return indices

def find_pivot(path, fs, prominence=218, threshold=0):
    data = pd.read_csv(path, skiprows=[0,1,2])
    column = data['Noraxon MyoMotion-Trajectories-Body center of mass-y (mm)']
    peaks, troughs = find_all_peaks(column, prominence, threshold)
    peak_1_indices = pivot_index_range(peaks[0], fs)
    peak_2_indices = pivot_index_range(peaks[1], fs)
    trough_1_indices = pivot_index_range(troughs[0], fs)
    trough_2_indices = pivot_index_range(troughs[1], fs)

    plt.figure()
    plt.plot(column) # plots data under the column name
    plt.show()

    return peak_1_indices, peak_2_indices, trough_1_indices, trough_2_indices


path = '2022-05-18-12-03_Pivots 2 (L-R).csv'
fs = 200
peak_1_indices, peak_2_indices, trough_1_indices, trough_2_indices = find_pivot(path, fs)

print(peak_1_indices)
print(peak_2_indices)
print(trough_1_indices)
print(trough_2_indices)
