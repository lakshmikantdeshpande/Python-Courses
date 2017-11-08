class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def setval(self, newval):
        self.val = newval

    def getval(self):
        return self.val

    # classmethod decorator makes sure that the calling method passes the class
    # instead of an instance
    # instance is not needed
    @classmethod
    def getcount(cls):
        return cls.count


a = InstanceCounter(2)
b = InstanceCounter(93)
c = InstanceCounter(587)

for _ in (a, b, c):
    print('Value of object: %s' % (_.getval()))
    print('count: %s' % (_.getcount()))
    # above stmt is equivalent to
    print('count: %s' % (InstanceCounter.count))
