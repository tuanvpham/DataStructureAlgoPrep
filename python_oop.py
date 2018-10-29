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



emp_1 = Employee('Kevin', 'Pham', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.fullname())
# This is how python works behind the scene
print(Employee.fullname(emp_1))

# Changing Employee.raise_amout affects emp_1 and emp_2, but changing emp_1.raise_amount only affects emp_1 which now emp_1 has a new attribute raise_amount
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
