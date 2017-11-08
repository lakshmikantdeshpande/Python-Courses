class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    # staticmethod will mark the methods which don't deal with the instance or class
    # eg. utility methods
    # no need of the instance. It belongs to class code
    @staticmethod
    def filterint(val):
        return val if isinstance(val, int) else 0


a = InstanceCounter(54)
b = InstanceCounter(46)
c = InstanceCounter(5246)
d = InstanceCounter('hello')

print(a.val)
print(b.val)
print(c.val)
print(d.val)
