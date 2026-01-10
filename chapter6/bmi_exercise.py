#!/usr/bin/python3

print("\nWelcome to my BMI checker")

weight = float(input("\nWhat is your weight in kg? "))

height = float(input("\nWhat is your height in meter? "))

bmi = (weight/height**2)

if bmi < 18.5:
    bmi = "underweight"
elif bmi >= 18.5:
    bmi = "healthyweight"
elif bmi > 24.9:
    bmi = "overweight"
else:
    bmi = "obesity"

print("\nYour body mass index is ", bmi)

print(input("\nDo you need my health advice?" ))
