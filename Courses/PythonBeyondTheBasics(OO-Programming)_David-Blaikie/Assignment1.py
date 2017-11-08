# Assignment 1


class MaxSizeList(object):
    def __init__(self, maxvalue):
        self.max = maxvalue
        self.lyst = []

    def push(self, value):
        if len(self.lyst) == self.max:
            self.lyst.pop(0)
        self.lyst.append(value)

    def get_list(self):
        return self.lyst


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('hey')
a.push('hi')
a.push('let\'s')
a.push('go')

b.push('hey')
b.push('hi')
b.push('let\'s')
b.push('go')

print(a.get_list())
print(b.get_list())
