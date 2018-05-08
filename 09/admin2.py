# !/usr/bin/env python3
# -*- coding:UTF-8 -*-

from user2 import User

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