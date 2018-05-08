# -*- coding:UTF-8 -*-

from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		a = randint(1, self.sides)
		return a

num = Die(20)

print("----------------------")
"""循环打印Die()结果多次"""

for t in range(10):
	print(num.roll_die())