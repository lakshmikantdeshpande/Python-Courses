import math

def square(number):
	return number * number


def sqrt(number):

	def sqrtHelper(guess):
		if (closeEnough(guess)):
			return guess
		else:
			return sqrtHelper(improve(guess))


	def closeEnough(guess):
		return (math.fabs((square(guess)) - number) < 0.001)


	def improve(guess):
		return average(guess, (number / guess))


	return sqrtHelper(1.0)


def average(x, y):
	return (x + y) / 2


if __name__ == "__main__":
	print(sqrt(9))
