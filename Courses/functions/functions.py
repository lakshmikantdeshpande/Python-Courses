def square(number):
	return number * number

def numVowels(strng):
	strng = strng.lower()
	count = 0
	for i in range(len(strng)):
		if strng[i] == "a" or strng[i] == "e" or \
			strng[i] == "i" or strng[i] == "o" or \
			strng[i] == "u":
			count += 1
	return count

if __name__ == "__main__":
	number = int(input("Enter a number: "))
	numsquare = square(number)
	print("The square of %d is %d" % (number, numsquare))

	strng = str(input("Enter a string: "))
	vowels = numVowels(strng)
	print("There are {} vowels in {}".format(vowels, strng))
