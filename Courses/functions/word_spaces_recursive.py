def explode(word):
	if len(word) <= 1:
		return word
	else:
		return word[0] + " " + explode(word[1:])


if __name__ == "__main__":
	print(explode("helloww"))

