def explode(word):
	if len(word) <= 1:
		return word
	else:
		return word[0] + " " + explode(word[1:])


def remove_duplicates(word):
	if len(word) <= 1:
		return word
	elif word[0] == word[1]:
		return remove_duplicates(word[1:])
	else:
		return word[0] + remove_duplicates(word[1:])

if __name__ == "__main__":
	print(explode("helloww"))
	print(remove_duplicates("heellowwloo"))

