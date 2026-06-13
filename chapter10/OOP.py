class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())  # Each calls its own speak()


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2,3)
v2 = Vector(1,4)
v3 = v1 + v2  # Uses _add_()
print(v3.x, v3.y)