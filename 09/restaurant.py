# -*- coding:UTF-8 -*-

class Restaurant():
	"""一次模拟餐馆运营的操作"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性name和type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""描述餐馆的烹饪类型"""
		print("The cuisine type is " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		"""描述餐馆是否在营业"""
		print(self.restaurant_name.title() + " is runing!")