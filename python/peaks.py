import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Define global variables here
FILE_NAME = 'data3.csv'
FILE_PATH = 'data/clean/'
SHOW_PLOT = False

# Import the cleaned data from csv
df = pd.read_csv(FILE_PATH + FILE_NAME)

time = df.iloc[:, 0].values
amp = df.iloc[:, 1].values

# Find the peaks in the signal
peaks, _ = find_peaks(amp, height=-10)

# Extract the time and amplitude of the peaks
time_peaks = time[peaks]
amp_peaks = amp[peaks]

# Compute the time between peaks
time_between_peaks = np.diff(time_peaks)

# Compute the mean and std of the time between peaks
avg_time = np.mean(time_between_peaks)
std_time = np.std(time_between_peaks)
err_time = std_time / np.sqrt(len(time_between_peaks))

# Print the results
print(f'Current file: {FILE_NAME}')
print(f'Average time between peaks: {avg_time:.3f} seconds')
print(f'Standard deviation of time between peaks: {std_time:.3f} seconds')
print(f'Error of time between peaks: {err_time:.3f} seconds')

# Plot the peaks for testing
if SHOW_PLOT:
    plt.plot(time, amp)
    plt.plot(time_peaks, amp_peaks, 'x')
    plt.show()
