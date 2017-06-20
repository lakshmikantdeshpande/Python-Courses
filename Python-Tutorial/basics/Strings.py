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

# using backticks
temp = 10
print(welcome + ' ' + `temp`)

# using repr()
print(welcome + repr(temp))
