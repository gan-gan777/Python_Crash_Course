# -*- coding:UTF-8 -*-

def show_magicians(names):
	"""向列表中的每一位魔术师发出简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

magicians = ['denver', 'eric', 'jerry']
show_magicians(magicians)