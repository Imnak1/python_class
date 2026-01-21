#!/usr/bin/python3
k = [1]
print(k)

#exercise on fstring
name = "John" 
age = 21 
print ("My name is {} and I am {} years old.".format(name,age)) 

#String formatting with arguments
print("Hello. My name is {name}, and I am a {occupation}.".format(occupation = "programmer", name = "John"))


#exercise on input 

name = str(input("Enter your name: ")) 

age = int(input("How old are you?: ")) 

sex = str(input("Enter your gender M or F: ")) 

location = str(input("Which city do you live in: ")) 

if sex == "M" or "m": 
    gender = "male" 
elif sex == "F" or "f": 
    gender = "female" 
else: 
    gender = "invalid" 

print ("{}, you are a {} old {} from {}.".format(name, age, gender, location))
print (f"{name}, you are a {age} old {gender} from {location}.")
