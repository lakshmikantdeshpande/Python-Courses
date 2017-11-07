class Name:
	
	# We don't need to create variables, directly define constructor
	def __init__(self, first, middle, last):
		self.first = first
		self.middle = middle
		self.last = last


	#to-string method
	def __str__(self):
		return self.first + ' ' + self.middle + ' ' + self.last
	

	def lastFirst(self):
		return self.last + ' ' + self.first + ' ' + self.middle
	

	def initials(self):
		return self.first[0] + '.' + self.middle[0] + '.' + self.last[0]


aName = Name('A', 'B', 'C')
print('Name of the object is ' + str(aName))
print('Name lastFirst ' + aName.lastFirst())
print('Initials ' + aName.initials())

