# https://www.youtube.com/watch?v=BJ-VvGyQxho
class Employee:

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		# access attributes of the class: self.raise_amount (from instance) or Employee.raise_amount (from class)
		self.pay = int(self.pay * self.raise_amount)

	# dunder (double underscore) or magic functions: don't need to invoke it directly. Invocation happens behind the scene
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullname, self.email)

	# operator overriding add method: __add__ for +, __sub__ for -, etc...
	def __add__(self, other):
		return self.pay + other.pay

	# Decorators: Getter, Setter
	# declare like a method, but with property, we can treat it as attribute
	
	# Getter
	@property
	def nickname(self):
		return 'nickname:{}'.format(self.first) 

	# Setter
	@nickname.setter
	def nickname(self, name):
		self.nickname = name


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		# super init: pass first, last, pay to superclass's init method
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super.__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--->', emp.fullname())


emp_1 = Employee('Kevin', 'Pham', 50000)
emp_2 = Employee('Test', 'User', 60000)

dev_1 = Developer('Tuan', 'Pham', 23000, 'Python')


print(emp_1.fullname())
# This is how python works behind the scene
print(Employee.fullname(emp_1))

# Changing Employee.raise_amout affects emp_1 and emp_2, but changing emp_1.raise_amount only affects emp_1 which now emp_1 has a new attribute raise_amount
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(dev_1.email)

print(emp_1 + emp_2)

print(emp_1.nickname)