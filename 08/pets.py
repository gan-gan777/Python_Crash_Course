# -*- coding:UTF-8 -*-

def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry')
describe_pet('willie', 'dog')