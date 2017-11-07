def isVowel(letter):
	if letter == "a" or letter == "e" or \
	 letter == "i" or letter == "o" or \
	 letter == "u":
		return True
	else:
		return False

	
def numVowels(strng):
	strng = strng.lower()
	count = 0
	for i in range(len(strng)):
			if isVowel(strng[i]):
				 count += 1
	return count

if __name__ == "__main__":
	strng = str(input("Enter a string: "))
	vowels = numVowels(strng)
	print("There are {} vowels in {}".format(vowels, strng))
