class Student:

	grades = []
	def __init__(self, name, id):
		self.name = name
		self.id = id
	

	def addGrade(self, grade):
		self.grades.append(grade)

	
	def showGrades(self):
		grs = ''
		for grade in self.grades:
			grs += str(grade) + ',' 
		return grs.rstrip(',')


student = Student('HannahBaker', '112')
student.addGrade(12)
student.addGrade(65)
student.addGrade(89)

print(student.showGrades())

