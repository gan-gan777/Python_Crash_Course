# -*- coding:UTF-8 -*-

# 首先，创建一个三明治的下单列表
#  另外，再创建一个用于存储已经制作完成的三明治的空列表
sandwich_orders = ['salmon', 'pastrami', 'ham', 'pastrami', 'beef', 'pastrami']
finished_sandwiches = []

# 指出熟食店的五香烟熏牛肉卖完了
print("Sorry, pastrami sold out.")

# 删除所有'pastrami'元素
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

# 制作每一个三明治，直到完成所有订单
#  将每个制作完成的三明治列表都移到已经制作完成的三明治列表中
while sandwich_orders:
	finished_sandwiche = sandwich_orders.pop()

	print("Finished sandwiche: " + finished_sandwiche.title())
	finished_sandwiches.append(finished_sandwiche)

# 显示所有已经制作完成的三明治
print("\nThe following sandwiches have been finished:")
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche.title())