motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + '.')

print(motorcycles)

motorcycles.insert(0, 'honda')
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")