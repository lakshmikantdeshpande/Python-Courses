class MyDict(dict):
    def __setitem__(self, key, value):
        print('Setting a key and value')
        dict.__setitem__(self, key, value)


dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print('{} = {}'.format(key, dd[key]))

print()
