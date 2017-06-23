import numpy as np

weight = [10, 20, 30, 40]
height = [1, 2, 3, 4]

# BMI = weight / (height * height)
# by using lists, we could not do all the operations at once
# numpy_basics helps us out here

np_weight = np.array(weight)
np_height = np.array(height)

bmi = np_weight / np_height ** 2

print(bmi)

# numpy will throw an error if the two arrays are of different type
# It allows arrays of only one type
# It converts to one type if multiple types are fed

temp = [1, "two", False]
print(np.array(temp))

# subsetting

print(bmi > 3)
