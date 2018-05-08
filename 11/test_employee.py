# -*- coding:UTF-8 -*-

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""针对Employee类的测试"""

	def setUp(self):
		"""
		创建一个员工的姓名和年薪增量，供使用的测试方法使用
		"""
		self.e1 = Employee('jerry', 'li')
		self.e2 = Employee('denver', 'kong')
		self.e2.give_raise(70000)

	def test_give_default_raise(self):
		"""测试默认增加年薪增量"""
		self.assertEqual(self.e1.salary, 5000)

	def test_give_custom_raise(self):
		"""测试自定义年薪增量"""
		self.assertEqual(self.e2.salary, 70000)


unittest.main()