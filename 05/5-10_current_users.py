current_users = ['Eric', 'Hardie', 'Qi', 'ZeJun', 'Jerry', 'DENVER', 'ADMIN']

new_users = ['Alise', 'Vince', 'Fei', 'Michael', 'Jerry', 'Denver', 'Admin']

# convert to lower char
current_users_lower = []
for current_user in current_users:
	current_user_lower = current_user.lower()
	current_users_lower.append(current_user_lower)
print(current_users_lower)

# convert to lower char
new_users_lower = []
for new_user in new_users:
	new_user_lower = new_user.lower()
	new_users_lower.append(new_user_lower)

print(new_users_lower)

for new_user_lower in new_users_lower:
	if new_user_lower in current_users_lower:
		print("The userName_" + new_user_lower + " is used, Please type other userName.")
	else:
		print("The userName_" + new_user_lower + " is not used.")