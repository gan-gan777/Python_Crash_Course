# -*- coding:UTF-8 -*-

class User():
	"""模拟描述用户基本信息"""
	def __init__(self, first, last, age, sex):
		"""初始化用户基本信息"""
		self.first_name = first
		self.last_name = last
		self.age = age
		self.sex = sex
		

	def describe_user(self):
		"""描述用户的基本信息"""
		full_name = self.first_name + self.last_name
		print("\nMy name is " + full_name.title() + ".")
		print("My sex is " + self.sex + ", and I'm " + str(self.age) + " years old.")

	def greet_user(self):
		"""向列表中的每位用户都发出简单的问候"""
		print("Thank for your attention," + self.first_name.title() + " " + self.last_name.title() + ".")

user_1 = User('denver', 'kong', 35, 'male') 

user_1.describe_user()
user_1.greet_user()