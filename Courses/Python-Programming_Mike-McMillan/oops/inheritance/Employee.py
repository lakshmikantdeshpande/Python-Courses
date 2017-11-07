class Employee:
	def __init__(self, name, payRate):
		self.name = name
		self.payRate = payRate

	
	def __str__(self):
		return self.name + ", " + str(self.payRate)
	

	def pay(self, hoursWorked):
		return self.payRate * hoursWorked


class Manager(Employee):
	def __init__(self, name, payRate, isSalaried):
		Employee.__init__(self, name, payRate)
		self.salaried = isSalaried


	def __str__(self):
		retStr = Employee.__str__(self)
		retStr += " Salaried: " + str(self.salaried)
		return retStr

	
	def pay(self, hoursWorked):
		if self.salaried:
			return self.payRate
		else:
			return self.payRate * hoursWorked


emp = Employee(" John ", 10)
print(emp)
print(" Gross Pay: ", str(emp.pay(40)))

man = Manager(" Jane", 1200, True)
print(man)
print(" Gross Pay: " + str(man.pay(40)))

seniorMan = Manager(" Dan", 20.00, False)
print(seniorMan)
print(" Gross Pay: " + str(seniorMan.pay(40)))

