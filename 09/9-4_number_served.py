# -*- coding:UTF-8 -*-

class Restaurant():
	"""一次模拟餐馆运营的操作"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性name和type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""描述餐馆的烹饪类型"""
		print("The cuisine type is " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		"""描述餐馆是否在营业"""
		print(self.restaurant_name.title() + " is runing!")

	def read_number_served(self):
		"""打印一条指出累计用餐人数的消息"""
		print("This restaurant has " + str(self.number_served) + " people on it.")

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
		
restaurant = Restaurant('The Sea', 'coconut chicken')

print(restaurant.restaurant_name.title() )
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(1254)
restaurant.read_number_served()

restaurant.increment_number_served(100)
restaurant.read_number_served()