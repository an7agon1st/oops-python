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
		self.pay= self.pay * self.raise_amt

	@classmethod # decorator. Changes fucnationality of the program. Now one method that follows is a class method

	def set_raise_amt(cls, amt):	#cls is the class variable. The class is automatically passed as first variable
		cls.raise_amt = amt;

	#using class method as a contructor. starts with 'from-...' by convention

	@classmethod

	def from_string(cls, emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)	# returns the object with the split variables parsing the string

	@staticmethod #follwing method is a static method

	def isWorkday(day): 	# doesn't pass class or instance as first argument
		if day.weekday == 5 or day.weekday==6:
			return False
		return True

emp_1 = Employee ('Tanzil' , 'Rahman' , 69000)
emp_2 = Employee ('Omair' , 'Sux' , 4200)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.10)	#since its a class method, it alters the raise_amt for the whole class
#can also run class methods from instances with the same effect

print(Employee.raise_amt)
print(emp_2.raise_amt)
print(emp_1.raise_amt)

emp_str_1 = 'John-Doe-690'
emp_str_2 = 'Jiju-Sawa-34'

cls_const_emp = Employee.from_string(emp_str_1)	# calls from_string which returns the class object

print(cls_const_emp.email)

import datetime
my_date = datetime.date(2016 , 7 , 10)

print(Employee.isWorkday(my_date))	# calling a static
