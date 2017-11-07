def countLetters(word):
	if len(word) < 1:
		return 0
	else:
		return len(word[0]) + countLetters(word[1:])


if __name__ == "__main__":
	sentence = ["Hello", "World"]
	print(sentence)
	print(countLetters(sentence))

