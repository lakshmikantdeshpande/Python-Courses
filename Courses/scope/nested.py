def sum_diff_sum(a, b):
	def sum(a, b):
		return a + b

	def diff(a, b):
		return a - b
	
	return sum(sum(a, b), diff(a, b))


if __name__ == "__main__":
	temp = sum_diff_sum(4, 5)
	print(temp)
