import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define global variables here
FILE_NAME = 'data3.csv'
FILE_PATH = 'data/'
SAVE_PATH = 'data/clean/'
SAVE_DATA = True

# Import the data from csv
df = pd.read_csv(FILE_PATH + FILE_NAME)

time = df.iloc[:, 0].values
amp = df.iloc[:, 1].values

# Convert string time to seconds
time = [datetime.strptime(t, '%M:%S.%f') for t in time]
time = [timedelta(minutes=t.minute, seconds=t.second, microseconds=t.microsecond).total_seconds() for t in time]
time = [t - time[0] for t in time]
time = np.array(time)

# Cut off the garbage at the two ends of the data
cutoff = int(len(time) * 0.1)
time = time[cutoff:-cutoff]
amp = amp[cutoff:-cutoff]

# Smooth the signal with a moving average filter
window_size = 5
smooth_amp = np.convolve(amp, np.ones(window_size)/window_size, mode='valid')
smooth_time = time[window_size-1:]

if SAVE_DATA:
    # Save the cleaned data to a new csv file
    cleaned_df = pd.DataFrame({'Time': smooth_time, 'Amplitude': smooth_amp})
    cleaned_df.to_csv(SAVE_PATH + FILE_NAME, index=False)
else:
    # Plot the data for testing
    plt.plot(time, amp)
    plt.plot(smooth_time, smooth_amp)
    plt.show()
