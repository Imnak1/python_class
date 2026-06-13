
class NewClass:
    
    """This is our first class. What it
    does is display a string text and a value of variable name"""
    def __init__(self,name):
        self.name = name
    
    def greeting(self):
        print("Hello", self.name)
        
        
myObject = NewClass("alagba")
#print(dir(myObject))
#Creates a new NewClass object
#myObject.greeting() # Calling function greeting()



class ComplexNumbers:
    
    def __init__(self, x = 0, y = 0):
        self.real = x
        self.imagined = y
    
    def getNumbers(self):

        print ("Complex numbers are:{0}+{1}j".format(self.real,self.imagined))
    
    def __repr__(self):
        print(f"the boy {self.real}, {self.imagined}")

    def alagba(self):
        print(f"the real number is {self.real}")

Object1 = ComplexNumbers(2, 3) #Creates a new ComplexNumbers object

Object1.getNumbers() #Calls getNumbers() function

Object2 = ComplexNumbers(10) #Creates another ComplexNumbers object

Object2.attr = 20 #Creates a new attribute 'attr'

print((Object2.real,Object2.imagined, Object2.attr))

#Object1.attr #Generates an error because c1 object doesn't have attribute

#print(dir(ComplexNumbers))
Object2.double = 100
print(Object2.real, Object2.attr, Object2.double)

Object2.__repr__()

Object1.alagba()