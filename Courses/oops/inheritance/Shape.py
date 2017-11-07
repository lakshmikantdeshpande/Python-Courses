class Shape:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	

	def __str__(self):
		return 'x: ' + str(self.x) + '  y: ' + str(self.y) + " "
	

	def move(self, xa, ya):
		self.x = self.x + xa
		self.y = self.y + ya


class Rectangle(Shape):
	def __init__(self, xcor, ycor, width, height):
		Shape.__init__(self, xcor, ycor) # Call the parent class's constructor, just like super()
		self.width = width
		self.height = height
	

	def __str__(self):
		retStr = Shape.__str__(self)
		retStr += 'width: ' + str(self.width) + " " + \
					'height: ' + str(self.height)
		return retStr + " "

rec = Rectangle(5, 10, 8, 9)
print(rec)
rec.move(10, 10)
print(rec)


