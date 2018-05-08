# -*- coding:UTF-8 -*-

def city_country(city, country):
	"""返回城市和国家名"""
	city_country = '\"' + city + ", " + country + '\"'
	return city_country.title()

tourist = city_country('beijing', 'china')
print(tourist)

tourist = city_country('santiago', 'chile')
print(tourist)

tourist = city_country('san francisco', 'USA')
print(tourist)
