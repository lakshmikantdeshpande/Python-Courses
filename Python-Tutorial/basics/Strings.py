from gi.module import maketrans

welcome = "welcome "
name = "Sachin"

# simple concatenation
welcome += name

print(welcome + name)

# comma separate for space separated output
print(welcome, name)

# print(number with string
# we have to convert the integer to string
# we can use str() or repr() or backticks(``)
number = 18
number = str(number)
print(welcome + number)

# using backticks eg. print(welcome + `temp`)
# not supported in Python 3.5, use repr() instead
temp = 10
print(welcome + ' ' + repr(temp))

# using repr()
print(welcome + repr(temp))

# translate method will replace specified characters in a string
inputtable = 'aeiou'
outputtable = '12345'

string = 'this is just a simple demo of translate method'
table = maketrans(inputtable, outputtable)
print(string.translate(table))
