#!/usr/bin/python3

import math

dict_1 = {"one" : 1, "two" : 2, "three" : 3, "four" : 4}
dict_2 = {"five" : 5, "six" : 6, "seven" : 7}
#print(math.cmp(dict_1, dict_2))
print("The total items for dictionary1 is", len(dict_1),  "\n and the sum of dictionary2 is", len(dict_2))

#checking str(dict) function
print(str(dict_1))

#How to check variable type?

print(type(dict_1))

#how to clear a dictionary?

#print(dict_1.clear())

dict_3 = dict_1.fromkeys("one")

print(dict_3)

print(dict_1.items())

print(dict_1.keys())

print(dict_2.values())

#how to use dict.get

print(dict_1.get("two"))

print( dict_1["two"])

dict_1.update(dict_2)

print(dict_1)



