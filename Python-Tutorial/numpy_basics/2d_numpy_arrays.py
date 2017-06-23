import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

print(type(np_height))

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.shape)

# if any one of the elements is a string, numpy will automatically convert all the elements to string as well

print(np_2d[0][3])
print(np_2d[0, 3])  # this will return the same element as above

# select few columns
print(np_2d[:, 1:3])  # it will select all rows, and columns from 1 to 3

# select weight of all family members
print(np_2d[1, :])
