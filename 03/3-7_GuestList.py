guest = ['Jobs', 'Bruce', 'Gloria']
print(guest.pop(-1) + "Can't reach!")

guest.insert(1, 'DuLei')


print("I find a bigger Table, but not! Just only invite two person!")
guest.insert(0, 'WJJ')
guest.insert(2, 'LXL')
guest.append('Ada')

first_sorry = guest.pop(0)
second_sorry = guest.pop()
third_sorry = guest.pop(1)
fourth_sorry = guest.pop(1)

print(first_sorry.title() + ', ' + "I'm so sorry!")
print(second_sorry.title() + ', ' + "I'm so sorry!")
print(third_sorry.title() + ', ' + "I'm so sorry!")
print(fourth_sorry.title() + ', ' + "I'm so sorry!")

print(guest)
print("Dear " + guest[0] + ":" + " "+ "Welcome home!")
print("Dear " + guest[1] + ":" + " "+ "Welcome home!")

del guest[0]
del guest[0]
print(guest)