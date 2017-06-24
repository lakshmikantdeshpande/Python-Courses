# np_baseball is available

# Import numpy
import numpy as np

np_baseball = np.array([[180, 78.4, 215, 102.7],
                        [129, 234, 548.4, 123.0]])

# Create np_height that is equal to the first row of  np_baseball
np_height = np.array(np_baseball[0, :])

# Print out the mean of np_height (Average)
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))
