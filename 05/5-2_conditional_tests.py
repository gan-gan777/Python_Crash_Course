car_num = 'BF46359'
if car_num == 'BF46359':
	print("Very well!")
else:
	print("waiting")

car = 'Audi'
if car.lower() == 'audi':
	print(car)

age = 18
if age == 30:
	print("This is a Woman!")
if age != 30:
	print("age != 30.")
if age > 30:
	print("age > 30.")
if age < 20:
	print("This is a girl.")
if age >= 18:
	print("You are already grown up.")
if age <= 20:
	print("But you still have to learn.")

Adults = ['Denver', 'Rachel']
Children = ['Doudou', 'DiDi', 'Denver']
member = 'Gloria'

if (member in Adults) and (member in Children):
	print("Denver")

if (member in Adults) or (member in Children):
	print(member)

if member not in Adults:
	print(member)