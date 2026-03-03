import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Define global variables here
FILE_NAME = 'old3.csv'
FILE_PATH = 'data/clean/'
SHOW_PLOT = True

# Define physical constants here
motor_speed = 50/61 * 1e-6
motor_err = motor_speed * 0.05

# Import the cleaned data from csv
df = pd.read_csv(FILE_PATH + FILE_NAME)

time = df.iloc[:, 0].values
amp = df.iloc[:, 1].values

# Find the peaks in the signal
peaks, _ = find_peaks(amp, height=-11)

# Extract the time and amplitude of the peaks
time_peaks = time[peaks]
amp_peaks = amp[peaks]

# Compute the time between peaks
time_between_peaks = np.diff(time_peaks)

# Compute the mean and std of the time between peaks
avg_time = np.mean(time_between_peaks)
std_time = np.std(time_between_peaks)
err_time = std_time / np.sqrt(len(time_between_peaks))

# Compute the wavelength of the laser
wavelength = 2 * motor_speed * avg_time * 1e9
wavelength_err = wavelength * np.sqrt((err_time / avg_time) ** 2 + (motor_err / motor_speed) ** 2)

# Print the results
print(f'Current file: {FILE_NAME}')
print(f'Average time between peaks: {avg_time:.3f} ± {err_time:.3f} seconds')
print(f'Standard deviation of time between peaks: {std_time:.3f} seconds')
print(f'Estimated wavelength of the laser: {wavelength:.3f} ± {wavelength_err:.3f} nm')

# Plot the peaks for testing
if SHOW_PLOT:
    plt.plot(time, amp)
    plt.plot(time_peaks, amp_peaks, 'x')
    plt.show()
