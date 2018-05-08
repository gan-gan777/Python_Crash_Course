#!/usr/bin/env python3

class Person:
    x = 'abc'
    def __init__(self, name, age=18):
        self.name = name
        self.y = age

    def show(self):
        print(self.name, self.y)

a = Person('tom')
b = Person('jerry', 20)

print(a.name, b.name)
print(a.x, b.x)

print(a.y, b.y)