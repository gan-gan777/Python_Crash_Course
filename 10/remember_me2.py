# !/usr/bin/env python3

# -*- coding:UTF-8 -*-

import json

# 如果一切存储了用户名，就加载它
#  否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What's your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username.title() + "!")
else:
	print("Welcome back, " + username.title() + "!")