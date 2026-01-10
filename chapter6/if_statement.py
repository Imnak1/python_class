#!/usr/bin/python3

x = 10
if (x == 10):
    print("x = 10")

    print(x)

if (x == 8):
    print("olodo")

else:
    print("gbayi")


Alagba = "available"
if (Alagba == "available"):
    print("\nwe are having python class")

else:
    print("\nwe won't have python class")


#if elif statement

age = int(input("Enter age to evaluate:"))

if age >= 18:
    agegroup = "Adult"
elif age >= 13:
    agegroup = "Teenager"
elif age >=0:
    agegroup = "Child"
else:
    agegroup = "Invalid"

print (agegroup)


#trial

age = int(input("\n\nEnter age to evaluate:")) 
if age >= 18: 
    print("\nAdult") 
elif age >= 13: 
    print("\nTeenager") 
elif age >=0: 
    print("\nChild")
else: 
    print("\nInvalid")


