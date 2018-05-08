# -*- coding:UTF-8 -*-

def print_names(filename):
	"""打印猫和狗的名称"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# 打印名字
		print(contents.rstrip())

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	print_names(filename)