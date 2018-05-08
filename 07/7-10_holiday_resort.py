# -*- coding:UTF-8 -*-

# 创建一个空的字典，用来存储独家圣地
resorts = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
	# 提示被调查者的名字和回答
	name = input("\nWhat's your name? ")
	response = input("Which resort would you like to paly someday? ")

	# 将答卷存储在字典中
	resorts[name] = response

	# 看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in resorts.items():
	print(name.title() + " would like to play " + response.title() + ".")
