number = input("Enter a number, and I'll tell you if it's an integer multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
	print("\nThe number " + str(number) + " is an integer multiple of 10.")
else:
	print("\nThe number " + str(number) + " is not an integer multiple of 10.")