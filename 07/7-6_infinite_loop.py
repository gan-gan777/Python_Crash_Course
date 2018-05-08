age = input("How old are you? ")

active = True
while active:
	# print("\nEnter 'quit' when you are finished.")
	# age = input("How old are you? ")

	if  age == 'quit':
		# active = False
		break
	elif int(age) < 3:
		print("\nYou're free.")
	elif (int(age) >= 3) and (int(age) < 12):
		print("\nYou need to pay 10 dollars.")
	elif (int(age) >= 12):
		print("\nYou need to pay 15 dollars.")