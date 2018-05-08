# -*- coding:UTF-* -*-

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey类的测试"""

	def setUp(self):
		"""
		创建一个调查对象和一组答案，供使用的测试方法使用
		"""
		question = "What is your salary?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = []