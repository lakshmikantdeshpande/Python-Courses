import numpy as np

weight = [10, 20, 30, 40, 100]
height = [1, 2, 3, 4, 2]

# BMI = weight / (height * height)
# by using lists, we could not do all the operations at once
# numpy_basics helps us out here

np_weight = np.array(weight)
np_height = np.array(height)

bmi = np_weight / np_height ** 2

print(bmi)

light = bmi < 21  # it will create a numpy array with booleans

print(light)

print(bmi[light])  # print only those values from BMI where values from light array are true (see the output to know)

print(light[2])

print(light[3:6])
