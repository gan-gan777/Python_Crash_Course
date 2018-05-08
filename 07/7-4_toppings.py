toppings = "\nTell me what you want:"
toppings += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(toppings)
	
	if message == 'quit':
		# active = False
		break
	else:
		print("Adding " + message + ".")