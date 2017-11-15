import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in values:
	sum = 0
	sum = sum + val
	pdb.set_trace()  # kinda like a breakpoint

print(sum)


"""
***Useful commands***
c = continue
n = next
s = step
l = show code
h = help
quit = quit
"""

