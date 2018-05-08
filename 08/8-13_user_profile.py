# -*- coding:UTF-8 -*-

def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first.title()
	profile['last_name'] = last.title()
	for key, value in user_info.items():
		profile[key] = value.title()
	return profile

user_profile = build_profile('denver', 'kong',
							location='shenzhen',
							field='computer')
print(user_profile)