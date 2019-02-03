class Employee:

	raise_amt = 1.04	# class variable

	emp_no =0

	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.emp_no += 1

	def fullName(self):
		return f'{self.first} {self.last}'

	def calcRaise(self):
		self.pay= self.pay * self.raise_amt		# class vars are accessed via class name or instance name (can also use Employee.raise_amt)
		#changing class var using instance, changes it only for that instance

# __dict__ shows the class/var's namespace

emp_1 = Employee('Tanzilur','Rahman', 696969)

print (emp_1.pay)

emp_1.calcRaise();

print (emp_1.pay)

print(Employee.emp_no)

