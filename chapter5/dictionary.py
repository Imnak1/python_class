#!/usr/bin/python3

#Creating dictionary

empty_dict = {}

integerkey_dict = {1: "Mango", 2: "Apple", 3: "Orange"}

mixedkey_dict = {"name": "John", 0: [2, 4, 3]}

print (integerkey_dict)
print (mixedkey_dict)

#Accessing dictionary elements

my_dict = {"name":"John", "age": 21, "occupation":"Programmer"}

print('\n\n', my_dict["name"])

print (my_dict.get('age'))

work = my_dict.get("occupation")

print (work)

print('\n',my_dict.get("name"),'\t', my_dict["age"],'\t', (work))

#updating dictionary element

student = {"name": "John Doe", "age": 25, "grade": "B+"}

print ("Before update:", student)

print ("\nChange age to 30:\nAdd Sex key:value pair")

student["age"] = 30

student["sex"] = "Male"

print ("\nAfter update:", student)

print ("Delete grade entry:")

del student["grade"]

print ("After deleting grade:", student)
