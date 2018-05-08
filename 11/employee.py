# -*- coding:UTF-8 -*-

class Employee():
	"""收集员工信息"""

	def __init__(self, first_name, last_name):
		"""存储员工属性信息，并为存储属性做准备"""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = 5000

	def get_formatted_name(self):
		"""返回整洁的姓名"""
		full_name = self.first_name + ' ' + self.last_name
		return full_name.title()

	def give_raise(self, add_salary):
		"""将年薪增加为指定的值"""
		self.salary = add_salary

	def read_salary(self):
		print("Your salary is " + str(self.salary) + ".")

# e1 = Employee('denver', 'kong')
# e1.give_raise(70000)

# print(e1.get_formatted_name())
# e1.read_salary()