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

restaurant = Restaurant('The Sea', 'coconut chicken')

print(restaurant.restaurant_name.title() )
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('donglaishun', 'shabu shabu')
print("\n" + restaurant2.restaurant_name.title() )
restaurant2.describe_restaurant()
restaurant2.open_restaurant()