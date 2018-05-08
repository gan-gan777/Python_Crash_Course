# -*- coding:UTF-8 -*-

def get_formatted_name(City, Country, population=''):
	"""生成城市和对应国家的名称"""
	if population:
		city_country = City + ', ' + Country + " - population " + str(population)
	else:
		city_country = City + ', ' + Country
	return city_country.title()