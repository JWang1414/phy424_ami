import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define global variables here
FILE_PATH = 'data/data1.csv'

# Import the data from csv
df = pd.read_csv(FILE_PATH)

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

# Plot the data for testing
plt.plot(time, amp)
plt.show()
