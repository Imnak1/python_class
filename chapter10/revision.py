class Animal:
    age = 4
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f"{self.name} makes this meow and age is {self.age}"

    def __repr__(self):
        print(f"the name of the animal is {self.name}")


animal1 = Animal('cat')

print(animal1.sound())
animal1.__repr__()
print(dir(animal1))
