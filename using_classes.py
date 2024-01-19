
# instance = class()
cities = list()
cities.append('Durham')
cities.append('Reno')
print(f"{cities[0] = }")   #  cities.__get_item__(...)
print()

a = 123
b = "456"
print(type(a), type(b))

class Animal:
    def run(self):
        print("Running")

a1 = Animal()
a2 = Animal()
a1.run()

class Dog(Animal):
    def bark(self):
        print("WOOF WOOF")

d = Dog()
d.bark()
d.run()

