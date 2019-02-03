class Employee:

	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		

	# chaging a variable to a method, (getters and setter in java)
	@property	
	def email(self):
		return f'{self.first.lower()}.{self.last.lower()}@email.com'

	@property
	def fullName(self):
		return f'{self.first} {self.last}'

	#making a setter method
	@fullName.setter
	def fullName(self, Name):
		first, last = Name.split(" ")
		self.first = first
		self.last = last

	#making a deleter
	@fullName.deleter
	def fullName(self):
		print('delete')
		self.first = None
		self.last = None

emp_1 = Employee('Tanzil', 'Rahman', 696969)
emp_2 = Employee('Omair', 'Sux', 420000)

# emp_1.first = 'John'
# wouldnt change email from init if there wasnt property decorator

#change first and last name if full name changed 
emp_1.fullName = 'Tanzilur Rahman'

print(emp_1.first)
print(emp_1.email)	# email method be accessed without paranthesis
print(emp_1.fullName)

del emp_2.fullName # using a deleter