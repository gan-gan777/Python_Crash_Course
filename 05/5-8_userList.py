users_list = ['Eric', 'Hardie', 'Qi', 'ZeJun', 'Jerry', 'Denver', 'Admin']

for user_list in users_list:
	if user_list.lower() == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + user_list.title() + ", thank you for logging in again.")