class MyClass:
    name = 'Muthu'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a + b)


x = MyClass("Muthu", 35)
print(x.name)
print(x.age)
x.sum(4, 5)
