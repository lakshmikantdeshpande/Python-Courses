class GetSet(object):
    instance_count = 0
    # Shouldn't be accessed/subclassed although it can be accessed with _ClassName__mangled_name
    __mangled_name = 'no privacy'

    def __init__(self, value):
        self._attrval = value  # private to the class, can be subclassed
        GetSet.instance_count += 1

    @property
    def var(self):
        print('Getting the "var" attribute')
        return self._attrval

    @var.setter
    def var(self, value):
        print('Setting the "var" attribute')
        self._attrval = value

    @var.deleter
    def var(self):
        print('Deleting the "var" attribute')
        self._attrval = None


cc = GetSet(5)
cc.var = 10
print(cc._attrval)
print(cc._GetSet__mangled_name)
