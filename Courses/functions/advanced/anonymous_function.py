# lambda form
# anonymous function

# def square(number):
# 	return number * number
# 
# This function is written as an anonymous function below:

if __name__ == "__main__":
	square = lambda x : x*x # lambda
	numbers = [1, 2, 3, 4]
	print(list(map(square, numbers)))

	print(list(map(lambda x : x*x, numbers))) # anonymous function

