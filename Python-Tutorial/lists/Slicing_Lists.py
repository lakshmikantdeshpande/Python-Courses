example = list('abcdefgh')
print(example)

# replace everything from index 4
example[4:] = 'vxyz'
print(example)

# alternative
example[:4] = list('lmno')
print(example)

# slice and insert
example[1:1] = list('123')
print(example)

example[1:5] = []
print(example)

example.append('loo')
print(example)

print(example.count('loo'))

poop = ['c', 'o', 'o', 'l']
example.extend(poop)
print(example)

print(poop.index('o'))

poop.insert(2, 'more poop')
print(poop)

poop.pop(2)
print(poop)

poop.remove('o')
print(poop)

poop.reverse()
print(poop)
