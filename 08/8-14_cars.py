# -*- coding:UTF-8 -*-

def make_car(manufacturer, model, **car_info):
	"""创建一个字典，其中包含我们知道的有关汽车的一切"""
	profile = {}
	profile['manufacturer'] = manufacturer.title()
	profile['model'] = model.title()
	for key, value in car_info.items():
		profile[key] = value
	return profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)