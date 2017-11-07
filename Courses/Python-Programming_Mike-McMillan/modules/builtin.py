import os
import math

files = os.popen("ls *.py")
for file in files:
	print(file, end = '')

print(math.fabs(-12230.5))

