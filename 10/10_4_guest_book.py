# !/usr/bin/env python3
# -*- coding:UTF-8 -*-

filename = 'guest_book.txt'

active = True
while active:
	your_name = input("Please enter your name: ")
	if your_name == 'quit':
		break
	else:
		print("Hello, " + your_name.title() + "!")
	with open(filename, 'a') as file_object:
		file_object.write(your_name + " has gone here.\n")
	