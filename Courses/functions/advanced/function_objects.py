def square(number):
	return number * number

if __name__ == "__main__":
	num = 2
	numsquare = square(num)  
	print(numsquare)

	sq = square  # sq is a function object, which stores the reference to sq
	numsquare = sq(num)
	print(numsquare)

