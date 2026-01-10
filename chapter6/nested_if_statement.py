#!/usr/bin/python3

#how to use nested if_statement?

number = float(input("Enter a number to evaluate: ")) 

if number >= 0: 
     if number == 0: 
          print (number, "is a Zero") 
     else: 
          print (number, "is a positive number") 
else: 
     print (number, "is a negative number")
