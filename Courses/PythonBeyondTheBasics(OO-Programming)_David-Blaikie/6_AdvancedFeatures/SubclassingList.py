class MyList(list):
    def __getitem__(self, index):
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0: raise IndexError
        if index > 0: index -= 1
        list.__setitem__(self, index, value)


x = MyList(['a', 'b', 'c'])

print(x)

x.append('spam')

print(x[1])
print(x[4])
