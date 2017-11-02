words = ['asdfW', 'WEREWDSAfdsafW', 'HeLlO']

print('Before using list comprehension')
print(words)

print('After using list comprehension')
print([word.lower() for word in words])
