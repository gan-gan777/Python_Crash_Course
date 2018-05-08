# -*- coding: UTF-8 -*-

dictionary = {
	'variable': '变量',
	'control structure': '控制结构，控制程序的执行次序',
	'continue': '在循环中直接判断下次循环',
	'break': '直接跳出循环',
	'pass':'占位符'
}

# for term in dictionary:
# 	# print(term + ':' + dictionary[term])
# 	print(term + '\n' + '	' + dictionary[term])

for k, v in dictionary.items():
	print(k + ": " + v)