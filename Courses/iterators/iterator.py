numbers = [1, 2, 3, 4, 5]
it = iter(numbers)
print(next(it))
print(next(it))

file_iterator = open('temp.txt', 'r')
print(next(file_iterator))

