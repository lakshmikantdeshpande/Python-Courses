from random import randint

try:
	temp = randint(0, 1)
	if temp == 1:
		open("hello.txt", "r")
	else:
		t = 7 / 0
except IOError:
	print("File does not exist")
except ZeroDivisionError:
	print("Can't divide by zero")
finally:
	print("Please try again")

