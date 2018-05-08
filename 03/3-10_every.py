everythings = ['hill', 'River', 'bruce', 'gloria', 'money', 'girl', 'animal', 'sex', 'gun']
print(everythings)
print(len(everythings))

print(everythings[7].title())
print("I like the " + everythings[7].title())

everythings.append('Sun')
print(everythings)

everythings.insert(1, 'Kungfu')
print(everythings)

del everythings[0]
print(everythings)

everythings.pop()
print(everythings)

everythings.pop(4)
print(everythings)

everythings.remove('gun')
print(everythings)

everythings.pop()
print(everythings)