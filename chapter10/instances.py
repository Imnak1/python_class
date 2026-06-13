
class Car:
    def __init__(self, brand):
         self.brand = brand

c1 = Car("Toyota")
print(c1.brand)


class Person:

    def __init__(self, name, age = None):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

    def oldage(self, age):
        self.age = age
        print("I am", self.age, "years old")

p1 = Person("Jao")

print(p1.name)
p1.greet()
p1.oldage(10)



class Employee:

    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_company(cls):
        print(cls.company)

Object1 = Employee("Jao")

Object1.show_company()
print(Object1.name)