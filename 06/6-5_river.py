rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'huanghe': 'china'
}

for river, country in rivers.items():
	print("\nRiver: " + river.title())
	print("Country: " + country.title())
	print("The " + river.title() + " runs through " + country.title() + ".")

