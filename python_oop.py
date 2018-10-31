# https://www.youtube.com/watch?v=BJ-VvGyQxho
class Employee:

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		print('{} {}'.format(self.first, self.last))

	def apply_raise(self):
		# access attributes of the class: self.raise_amount (from instance) or Employee.raise_amount (from class)
		self.pay = int(self.pay * self.raise_amount)


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


