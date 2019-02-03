
class ToBeIgnored:
	pass
# the class is ignored for now. Without pass, it gives an error

class Employee:

	def __init__(self):
		pass

	# self is the instance of the class that is passed to itself automatically for each method in the class

	def __init__ (self, first, last, pay):	#constructor for the class
	
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullName(self):
		return f"{self.first} {self.last}"

	def full_name(self):
		return f"{self.first} {self.last}"


# emp_1 = Employee();
# emp_2 = Employee();

# print (emp_1)
# print (emp_2)
# # emp_1 and emp_2 are instances of the class Employee and are called instance variables

# emp_1.first = "Tanzilur"
# # can create variables related to instance variables just like that if theres no _ _init_ _

emp_3 = Employee('Omair','Sux',2)

print(emp_3.email) 

print(emp_3.fullName())

print(Employee.full_name(emp_3)) # the instance gets passed automatically so can be passed by passing it by calling method via class name and passing the instance to it