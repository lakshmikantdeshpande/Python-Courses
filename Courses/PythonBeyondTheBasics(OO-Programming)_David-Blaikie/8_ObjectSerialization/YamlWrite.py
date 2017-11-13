import yaml

class MyClass(object):
	classvar = 10

	def __init__(self, val):
		self.val = val

	def increment(self):
		self.val += 1


x = MyClass(4)
x.increment()
x.increment()

with open('obj.yaml', 'w') as handle:
	yaml.dump(x, handle)

with open('obj.yaml') as handle:
	inst = yaml.load(handle)

print(inst.val)

