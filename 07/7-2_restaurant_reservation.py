count = "Tell me people counting, and I will check for availability to you."
count += "\nHow many people do you have? "

counting = input(count)
counting = int(counting)

if counting <= 8:
	print("There are places in the restaurant.")
else:
	print("There are not places in the restaurant.")