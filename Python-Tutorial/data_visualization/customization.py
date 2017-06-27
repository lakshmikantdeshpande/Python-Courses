import matplotlib.pyplot as plt

year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
population = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Simple plot
# plt.plot(year, population)

# Fill with color
plt.fill_between(year, population, 0, color='green')

plt.xlabel('Year')
plt.ylabel('Population')
plt.title("World population projections")

plt.yticks([0, 20, 40, 60, 80, 100],
           ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()
