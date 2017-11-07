class Rational:
	
	def __init__(self, x, y):
		numer = x
		if y == 0:
			raise ZeroDivisionError()
		else:
			denominator = y
	
try:
	rational = Rational(4, 1)
	rational = Rational(3, 0)
except:
	print("Can't have a rational number with 0 as denominator")

