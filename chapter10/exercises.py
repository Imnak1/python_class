class kalculate:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add (self):
        return self.num1 + self.num2

    def substract (self):
        return self.num1 - self.num2

object1 = kalculate(4,2)
print(object1.add())

