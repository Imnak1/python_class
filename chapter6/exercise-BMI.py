#!/usr/bin/python3

bmi= int(input("enter your BMI"))

if bmi < 18.5:
    bmi = "Underweight"
elif bmi >= 18.5:
    bmi = "Healthy weight"
elif bmi > 24.9:
    bmi = "Overweight"
else:
    bmi = "Obesity"
