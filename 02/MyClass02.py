class MyClass:
    x = 123

    def foo(self):
        print(self.x)

print(MyClass)
print(MyClass.__name__)
print(MyClass.x)
print(MyClass.foo)

mycls = MyClass()