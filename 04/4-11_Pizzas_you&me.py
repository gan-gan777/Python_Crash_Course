my_pizzas = ['Chicken', 'Durian', 'Beef']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Double')
friend_pizzas.append('Mango')

print("My favorite pizza are:")
print(my_pizzas)

for my_pizza in my_pizzas:
	print("I like " + my_pizza.lower() + " pizza.")

print("\nMy friend's favorite pizza are:")
print(friend_pizzas)

for friend_pizza in friend_pizzas:
	print("My friend like " + friend_pizza.lower() + " pizza.")

print("I really love pizza.")
