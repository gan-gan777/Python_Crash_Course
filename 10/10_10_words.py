# !/usr/bin/env python3
# -*- coding:UTF-8 -*-

filename = '57045_0.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	pass
else:
	# 计算单词'the'在文件中出现了几次
	line = contents.lower()
	num_words = line.count('the')
	print("The file " + filename + " has about " + str(num_words) + " 'the' word!")
