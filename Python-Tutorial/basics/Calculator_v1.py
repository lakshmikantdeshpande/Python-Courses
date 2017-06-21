# Simple calculator using basic Python
import math

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition: " + str(x + y))
print("Subtraction: " + str(x - y))
print("Multiplication: " + str(x * y))
print("Division: " + str(x / y))
print("Floor Division: " + str(x // y))
print("Power: " + str(x ** y))
print("Modulus: " + str(x % y))
print("Square Root: " + str(math.sqrt(x)))
print("Floor of " + str(x) + " / 2.9: " + str(math.floor(x / 2.9)))
print("Ceil of " + str(x) + " / 2.9: " + str(math.ceil(x / 2.9)))
