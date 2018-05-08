# -*- coding:UTF-8 -*-

class User():
	"""模拟描述用户基本信息"""
	def __init__(self, first, last, age, sex):
		"""初始化用户基本信息"""
		self.first_name = first
		self.last_name = last
		self.age = age
		self.sex = sex
		self.login_attempts = 0
		

	def describe_user(self):
		"""描述用户的基本信息"""
		full_name = self.first_name + self.last_name
		print("\nMy name is " + full_name.title() + ".")
		print("My sex is " + self.sex + ", and I'm " + str(self.age) + " years old.")

	def greet_user(self):
		"""向列表中的每位用户都发出简单的问候"""
		print("Thank for your attention," + self.first_name.title() + " " + self.last_name.title() + ".")

	def read_login_attempts(self):
		"""打印一条尝试登陆次数的消息"""
		full_name = self.first_name + ' ' + self.last_name
		print("\n" + full_name.title() + " login attempt is alreadly " + str(self.login_attempts) + ".")

	def increment_login_attempts(self, counts):
		"""将尝试登陆次数增加指定的次数"""
		if counts >= 0:
			self.login_attempts += counts
		else:
			print("You can't roll back an counts!")

	def reset_login_attempts(self, count):
		"""重置登陆次数"""
		self.login_attempts = 0



user_1 = User('denver', 'kong', 35, 'male') 
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts(4)
user_1.read_login_attempts()

