favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

# for name, languages in favorite_languages.items():
# 	print("\n" + name.title() + "'s favrite languages are:")
# 	for language in languages:
# 		print("\t" + language.title())

for name, languages in favorite_languages.items():
	if len(languages) < 2:
		# pass
		print("\n" + name.title() + "'s favrite languages is:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favrite languages are:")
		for language in languages:
			print("\t" + language.title())