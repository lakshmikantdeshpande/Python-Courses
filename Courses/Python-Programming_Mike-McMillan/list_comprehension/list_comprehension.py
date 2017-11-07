grades = [1, 325, 234, 315, 353, 431]
print('Before modifying the list:')
print(grades)

#   for i in range(len(grades)):
#       grades[i] = grades[i] + 5

grades = [grade + 5 for grade in grades]
print('After modifying the list:')
print(grades)
