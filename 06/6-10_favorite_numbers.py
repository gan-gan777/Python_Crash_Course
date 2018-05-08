favotite_numbers = {
	'Denver': [7, 8, 666],
	'Eric': [9, 10, 20],
	'Jerry': [10, 100, 21],
	'Hardie': [2, 50, 60],
	'Qi': [8, 7, 6],
	}

for name, numbers in favotite_numbers.items():
	print("\n" + name.title() + "'s favotite numbers are:")
	for number in numbers:
		print("\t" + str(number))
