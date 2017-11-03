def ftoc(temp):
	return (temp - 32.0) * (5.0 / 9.0)


def ctof(temp):
	return temp * (9.0 / 5.0) + 32.0


def convert(temp, toScale):
	toScale = toScale.lower()
	return ftoc(temp) if toScale == "c" else ctof(temp);


if __name__ == "__main__":
	temp = int(input("Enter a temperature: "))
	scale = input("Enter a scale to convert to: ")
	converted_temperature = convert(temp, scale)
	print(temp, converted_temperature, scale)

