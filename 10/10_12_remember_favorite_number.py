# -*- coding:UTF-8 -*-

import json

# 如果一切存储了数字，就加载它
#  否则，就提示用户输入数字并存储它
filename = 'favorite_number1.json'
try:
	with open(filename) as f_obj:
		favorite_number1 = json.load(f_obj)
except FileNotFoundError:
	favorite_number1 = input("What is your favorite number: ")
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number1, f_obj)
else:
	print("I know your favorite number！It's " + favorite_number1 + ".")