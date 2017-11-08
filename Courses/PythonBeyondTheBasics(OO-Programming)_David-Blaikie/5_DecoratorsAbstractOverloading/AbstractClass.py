import abc


# abc provides a way to create abstract classes
class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        """Set a value in an instance"""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from the instance"""
        return


class MyClass(GetterSetter):
    # def set_valz(self, val): << should throw an error
    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val


x = MyClass()
x.set_val(5)
print(x.get_val())
