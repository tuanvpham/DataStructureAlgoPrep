# https://www.youtube.com/watch?v=BJ-VvGyQxho
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		print('{} {}'.format(self.first, self.last))


emp_1 = Employee('Kevin', 'Pham', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.fullname())

print(Employee.fullname(emp_1))
