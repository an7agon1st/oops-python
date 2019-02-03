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

	#__repr__ used for debugging and logging and stuff. Meant for other developers (called with repr(object))

	#__str__ meant for end user (called with str(object))

	#str uses repr as a fallback
	#so, good to have repr as fall back

	def __repr__(self):
		return f'Employee ({self.first} , {self.last}, {self.pay})'	# rule of thumb to return Object code

	def __str__ ( self ):	# for the end user
		return f'{self.fullName()} - {self.email}'

	def __add__ (self, other): # func which adds 2 emps salary with just a plus
		return (self.pay + other.pay) 
	# special methods allow some functions to be used built within python also for operator overloading
	# opearator overloading:
	# 1 + 2 = 3
	# 'a' + 'b' = 'ab'

emp_1 = Employee ('John', 'Doe' , 1000000)
emp_2 = Employee ('Tanzil', 'Rahman', 696969)

print(repr(emp_1))

print(str(emp_1))

print(emp_1) # goes to str method, wouldve displayed raw object otherwise

print (emp_1 + emp_2)	# prints combined salaries, would give error without __add__ method

# look up dunder method in doc

#return NotImplemented throws job to other object if it knows how to handle the task else prints an error

