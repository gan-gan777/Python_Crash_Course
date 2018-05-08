# -*- coding:UTF-8 -*-

import unittest
from city_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试city_functions.py"""

	def test_city_country(self):
		"""能够正确地处理Santiage, Chile这样的名称吗？"""
		formatted_name = get_formatted_name('Santiago', 'Chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')

	def test_city_country_population(self):
		"""能够正确地处理Santiage, Chile - population 5000000这样的形式吗？"""
		formatted_name = get_formatted_name(
			'Santiago', 'Chile', 5000000)
		self.assertEqual(formatted_name, 'Santiago, Chile - Population 5000000')

unittest.main()