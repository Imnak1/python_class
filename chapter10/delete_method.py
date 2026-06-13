
class ComplexNumbers:
     def __init__(self, x = 0, y = 0):
          self.real = x
          self.imagined = y
          

     def getNumbers(self):
          print ("Complex numbers are:{0}+{1}j".format(self.real,self.imagined))

Object1 = ComplexNumbers(2,3) #Creates a new ComplexNumbers object
print(Object1)

Object1.getNumbers() #Calls getNumbers() function

Object2 = ComplexNumbers(10) #Creates another ComplexNumbers object

Object2.attr = 20 #Creates a new attribute 'attr'

print ((Object2.real, Object2.imagined, Object2.attr))

###del ComplexNumbers.getNumbers###

Object1.getNumbers()
