#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Restaurant():
	"""一次模拟餐馆运营的操作"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性name和type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""描述餐馆的信息"""
		print("The restaurant's name is " + self.restaurant_name + ", and it's type is " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		"""描述餐馆是否在营业"""
		print(self.restaurant_name.title() + " is opening!")

	def read_number_served(self):
		"""打印一条指出累计用餐人数的消息"""
		print("Now, this restaurant has " + str(self.number_served) + " people in it.")

	def set_number_served(self, conut):
		"""
		将累计用餐人数设定为指定的值
		禁止将累计用餐人数往回调打
		"""
		if conut >= self.number_served:
			self.number_served = conut
		else:
			print("You can't roll back an conuts!")

	def increment_number_served(self, conuts):
		"""将累计用餐人数增加指定的数量"""
		if conuts >= 0:
			self.number_served += conuts
		else:
			print("You can't roll back an conuts!")

class IceCreamStand(Restaurant):
	"""冰淇淋🍦小店的独特之处"""

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['qiaokeli', 'caomei', 'mangguo']

	def describe_iceCream(self):
		"""打印各种冰淇淋组成列表"""
		print("The restaurant has many ice-cream:")
		for flavor in self.flavors:
			print(flavor)

restaurant = Restaurant('KFC', 'fast food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served(100)
restaurant.set_number_served(50)
restaurant.read_number_served()

ice_cream = IceCreamStand('tiantian', 'Ice')
ice_cream.describe_iceCream()

		