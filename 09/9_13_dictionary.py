# -*- coding:UTF-8 -*-

from collections import OrderedDict

dictionarys = OrderedDict()

dictionarys['variable'] = '变量'
dictionarys['control structure'] = '控制结构，控制程序的执行次序'
dictionarys['continue'] = '在循环中直接判断下次循环'
dictionarys['break'] = '直接跳出循环'
dictionarys['pass'] = '占位符'
dictionarys['int'] = '整数'

for k, v in dictionarys.items():
	print(k + " : " + v)