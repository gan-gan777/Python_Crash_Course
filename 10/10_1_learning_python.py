with open('learning_python.txt') as file_object:
	# contects = file_object.read()
	# print(contects)
	lines = file_object.readlines()


for line in lines:
	print(line.rstrip())