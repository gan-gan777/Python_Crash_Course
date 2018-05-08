# -*- coding:UTF-8 -*-

import json

def get_stored_username():
	"""如果存储了用户，就获取它"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username.title()

def get_new_username():
	"""提示用户输入用户名"""
	username = input("What's your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username.title()

def greet_user():
	"""问候用户，并指出其名字"""
	username = get_stored_username()
	if username:
		ask = input("Is the username " + username + " right? (y/n)")
		if ask == 'y':
			print("Welcome back, " + username.title() + "!")
		else:
			username = get_new_username()
			print("We'll remember you when you come back, " + username.title() + "!")	
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username.title() + "!")

greet_user()

