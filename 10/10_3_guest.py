filename = 'guest.txt'

with open(filename, 'w') as file_object:
	login = input("What's your name?")
	file_object.write(login.title())