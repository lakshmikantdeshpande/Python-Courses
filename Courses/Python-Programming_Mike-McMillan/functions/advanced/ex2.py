# In My Humble Opinion => IMHO

def first(word):
	return word[0]


def acronym(words):
	acro = ''
	acronym = acro.join(list(map(first, words))).upper()
	return acronym	


if __name__ == "__main__":
	words = ['in', 'my', 'humble', 'opinion']
	print(acronym(words))

