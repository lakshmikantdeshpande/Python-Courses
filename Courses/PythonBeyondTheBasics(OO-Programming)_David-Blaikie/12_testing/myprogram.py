import sys

def doubleit(x):
	if not isinstance(x, (int, float)):
		raise TypeError
	var = x * 2
	return var

if __name__ == "__main__":
	input_val = sys.argv[1]
	doubled = doubleit(input_val)

