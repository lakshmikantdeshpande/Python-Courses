import sys

def doubleit(x):
	if not isinstance(x, (int, float)):
		raise TypeError
	var = x * 2
	return var

def doublelines(filename):
	with open(filename) as fh:
		newlist = [str(doubleit(int(val))) for val in fh]
	with open(filename, 'w') as fh:
		fh.write('\n'.join(newlist))

if __name__ == "__main__":
	input_val = sys.argv[1]
	doubled = doubleit(input_val)

