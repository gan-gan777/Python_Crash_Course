print("Give me two number, and I'll addition them.")
print("Enter 'q' tu quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("You need to Enter int type!")
	else:
		print(answer)