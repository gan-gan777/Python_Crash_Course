# -*- coding:UTF-8 -*-

# 定义起司和饼干的函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count # 打印”你有几个起司“
	print "You have %d boxes of crackers!" % boxes_of_crackers  # 打印”你有几盒饼干“
	print "Man that's enough for a party!"  # 这个人足够办一个聚会了
	print "Get a blanket.\n"  # 准备了一个毯子

# 直接调用函数
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# 或者，使用变量
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# 甚至可以使用运算
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 并且可以结合变量和运算
print "And we can combin the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)