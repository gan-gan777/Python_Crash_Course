cities = {
	'beijing': {
		'country': 'china',
		'population': '22 million',
		'fact': 'smog',
		},
	'paris': {
		'country': 'france',
		'population': '11 million',
		'fact': 'romantic',
		},
	'new York': {
		'country': 'US',
		'population': '9 million',
		'fact': 'skyscrapers',
		},
}

del cities['new York']

cities['tokyo': {
		'country': 'Japan',
		'population': '37 million',
		'fact': 'AV',
		},
]

for city, city_info in cities.items():
	print("\nCity: " + city.title())
	population = city_info['population']
	fact = city_info['fact']

	print("\tPopulation: " + population)
	print("\tFact: " + fact.title())