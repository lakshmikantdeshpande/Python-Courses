import abc


class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print('GetSetInt object {} only accepts integer values'.format(id(self)))


class GetSetList(GetSetInt):
    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print('GetSetList object, len({}), stores '
              'history of values set'.format(self.vallist))


gsint = GetSetInt(57)
gsint.set_val(5)
print(gsint.get_val())
gsint.showdoc()

print()

gslist = GetSetList(98)
print(gslist.get_val())
gslist.set_val(45)
print(gslist.get_vals())
gslist.showdoc()
