# !/usr/bin/env python3
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
		full_name = self.first_name + ' ' + self.last_name
		print("\nMy name is " + full_name.title() + ".")
		print("My sex is " + self.sex + ", and I'm " + str(self.age) + " years old.")

	def greet_user(self):
		"""向列表中的每位用户都发出简单的问候"""
		print("Thank for your attention," + self.first_name.title() + " " + self.last_name.title() + ".")

class Admin(User):
	"""管理员有一些特殊属性"""

	def __init__(self, first, last, age, sex):
		"""初始化父类属性，再初始化管理员的特有属性"""

		super(Admin, self).__init__(first, last, age, sex)
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		"""打印一条显示管理员权限的消息"""
		print("The below is admin's privileges list: ")
		for privilege in self.privileges:
			print(privilege)