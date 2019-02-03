class Employee:

	raise_amt = 1.04	# class variable

	emp_no = 0

	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.emp_no += 1

	def fullName(self):
		return f'{self.first} {self.last}'

	def calcRaise(self):
		self.pay= self.pay * self.raise_amt

class Developer (Employee): # inherits Employee class
	raise_amt = 1.11	#will consider Developer's raise amt instead of employee's

	#making a subclass init method with more arguments than the super class
	def __init__ (self, first, last,pay, prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

class Manager (Employee):
	def __init__ (self, first, last,pay, employees = None):	# employees contains a list of employees working under the manager
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def addEmployee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)	

	def remEmployee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def printEmployee(self):
		if emp in self.employees:
			print('-->', emp.fullName())

emp_1 = Developer ('Tanzil', 'Rahman', 696969, 'Java')
emp_2 = Developer ('Amir', 'Mohibi', 42000, 'C')

print(emp_1.email)

print(emp_1.pay)
emp_1.calcRaise()
print(emp_1.pay)

print(emp_1.prog_lang)

mgr_1 = Manager ('John', 'Doe', 7900, [emp_2])

print(mgr_1.email)

mgr_1.addEmployee(emp_1)

#mgr_1.printEmployee() check this out l8r

print(isinstance(mgr_1, Manager))

print(issubclass(Developer, Employee))


