# map filter reduce are high order functions

def square(number):
	return number * number


def even(number):
	return number % 2 == 0


def sum(x, y):
	return x + y


if __name__ == "__main__":
	numbers = [1, 2, 3]
	print(numbers)

	# map
	numbers_sq = list(map(square, numbers))
	print(numbers_sq)

	# filter
	numbers = list(range(0, 11))
	print(numbers)
	evens = list(filter(even, numbers))
	print(evens)
	
	# Reduce
	import functools
	numbers = list(range(0, 11))
	sum = functools.reduce(sum, numbers)
	print("The sum of the given range is ", str(sum))

