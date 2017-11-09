mydictionary = {'a': 5, 'b': 8}
key = str(input('Please enter a key: '))

try:
    print(mydictionary[key])
except KeyError:
    print('KeyError: Oops.. Key doesn\'t exist')

print('Program continues...')
