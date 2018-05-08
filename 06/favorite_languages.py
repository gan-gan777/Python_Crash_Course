favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# print("Sarah's favorite_language is " +
# 	favorite_languages['sarah'].title() +
# 	".")

# for name, language in favorite_languages.items():
# 	# print("\nName: " + name.title())
# 	# print("language: " + language.title())
# 	print(name.title() + "'s favorite_language is " + 
# 		language.title() + ".")

# for name in favorite_languages.keys():
# for name in favorite_languages:
# 	print(name.title())

friends = ['phil', 'sarah', 'erin']
for name in favorite_languages.keys():
	# print(name.title())
	if name in friends:
		print(name.title() + ", think you for taking the poll!")
	else:
		print(name.title() + ", please take our poll!")

# 	if name in friends:
# 		print(" Hi " + name.title() +
# 			", I see your favorite language is " +
# 			favorite_languages[name].title() + "!")
# if 'erin' not in favorite_languages.keys():
# 	print("\nErin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
	# print(name.title() + ", think you for taking the poll!")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())