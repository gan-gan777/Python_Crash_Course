favorite_places = {
	'Denver': ['maldives', 'us'],
	'Rachel': ['Japan', 'Egypt'],
	'Doudou': ['Shunde', 'Shenzhen'],
}

for name, places in favorite_places.items():
	print("\n" + name.title() + "'s favorite places are:")
	for place in places:
		print("\t" + place.title())