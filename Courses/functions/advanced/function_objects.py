def square(number):
	return number * number

if __name__ == "__main__":
	num = 2
	numsquare = square(num)  
	print(numsquare)

	sq = square  # sq is a function object, which stores the reference to sq
	numsquare = sq(num)
	print(numsquare)

	# map is a higher order function (Functional Programming)
	numbers = [1, 2, 3, 4]
	numbers_squares = list(map(square, numbers))
	print(numbers_squares)

