# -*- coding:UTF-8 -*-

def describe_city(name, country='china'):
	"""显示shirt的信息"""
	print("\n" + name.title() + " is in " + country.upper() + ".")

describe_city('beijing')
describe_city(country='USA', name='Los Angeles')
describe_city('shenzhen')