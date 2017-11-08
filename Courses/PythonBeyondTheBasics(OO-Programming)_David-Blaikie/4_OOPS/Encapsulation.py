# setter and getter methods ensure the integrity of the data
# with encapsulation (This class doesn't represent a fully encapsulated class)


class MyClass(object):
    def set(self, val):
        self.val = val

    def get(self):
        return self.val


instance = MyClass()
instance.set(1)

print(instance.get())
