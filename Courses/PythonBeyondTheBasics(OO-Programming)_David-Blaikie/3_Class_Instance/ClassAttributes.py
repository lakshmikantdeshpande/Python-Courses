class InstanceCounter(object):
    count = 0  # Class Attribute

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def setval(self, newval):
        self.val = newval

    def getval(self):
        return self.val

    def getcountClass(self):
        return InstanceCounter.count

    def getcountInstance(self):
        return self.count


a = InstanceCounter(10)
b = InstanceCounter(20)
c = InstanceCounter(30)

for _ in (a, b, c):
    print('val of obj: %s' % _.getval())  # Prints initial values
    print('count (from instance): ', _.getcountInstance())  # Prints 3 (class variable)
    print('count (from class): ', _.getcountClass())  # Prints 3 (class variable)
    print()
