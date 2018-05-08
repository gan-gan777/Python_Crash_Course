# -*- coding:UTF-8 -*-

def make_great(before_magicians, after_magicians):
	"""
	在每一位魔术师前面添加定于’The Great‘
	添加定语后，都将其移到列表after_magicians中
	"""
	while before_magicians:
		current_magician = before_magicians.pop()

		# 模拟添加定语的过程
		print("The Great magician: " + current_magician.title())
		after_magicians.append("The Great " + current_magician)

def show_after_magicians(after_magicians):
	"""显示处理后的列表"""
	print("\nThe following magicians have been changed:")
	for after_magician in after_magicians:
		print(after_magician)


before_magicians = ['denver', 'eric', 'jerry']
after_magicians = []

make_great(before_magicians[:], after_magicians)
show_after_magicians(after_magicians)

print("\n")
print(before_magicians)
print(after_magicians)