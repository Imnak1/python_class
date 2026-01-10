#!/usr/bin/python3
x = 7
print (x, "is of type", type(x))
y = 7.0
print (y, "is of type", type(y))
z = 1+2j
print ("is", z, "a complex number?", isinstance(1+2j,complex))

x, y, z = 5.7, 10, "3.5j"

print (x, "is of type", type(x), y, "is of type", type(y), "and", z, "is a",
type(z))

x = int(x); y = float(y); z = complex (z)

print ("After coercion, x new value is", x, ", y's new value is", y, "and", z, "is of a type", type(z))

#MATHEMATICAL FUNCTIONS
age = -50
print(abs(age))

import math
amt = 90.54
print(math.floor(amt))

a = 2
print(math.exp(a))


import math
b = 16
print(math.sqrt(b))




