import random


class InstanceAttributes(object):
    def dothis(self):
        self.rand = random.randint(11, 101)


instance = InstanceAttributes()
instance.dothis()
print(instance.rand)
