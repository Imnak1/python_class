#!/usr/bin/python3

print("\nwelcome on board")
lst_all = []
for i in range(3):

    dict_name = {}
    name = input("\nwhat is your name? ")

    age = input("\nwhat is your age? ")

    position = input("\nwhat is your position? ")

    dict_name["name"] = name
    dict_name["age"] = age
    dict_name["position"] = position

    print(name, age, position)
    print(dict_name)
    lst_all.append(dict_name)
print(lst_all)
