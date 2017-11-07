import callee


def square(a):
	return a ** 2


print(square(2))
print(callee.square(2))
