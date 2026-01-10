#!/usr/bin/python3

print("\nYou are welcome to my villa")

name = input("\nWhat is your name? ").title()

print("\nWelcome",name)

answer= input("\nDo you want to enter inside? Yes/No ")

if (answer == "Yes" or answer == "YES" or answer == "yes"):
    print("\nWelcome into my house.")
    answer2 = input("\nDo you want food? Yes/No ")
    if (answer2 == "Yes" or answer2 == "YES" or answer2 == "yes"):
        print("\nTurn left and enter the corridor")
        answer3 = input("\nAre you in the corridor? Yes/No ")
        if answer3 == "Yes":
            print("\nEnter the door by your right side")
            answer4 = input("\nAre you there? Yes/No ")
            if answer4 == "Yes":
                print("\nWelcome to my kitchen")
                food = ["Beans","Rice", "Chicken", "Turkey", "Salad"]
                print("\n",food)
                answer5 = input("\nWhat do you care for? ")
                if answer5 == "Beans":
                    print("\nCheck inside the pot for ",answer5)
                elif answer5 == "Rice":
                    print("\nCheck the cooler for the ",answer5)
                elif answer5 == "Chicken":
                    print("\nCheck inside the airfryer ",answer5)
                elif answer5 == "Turkey":
                    print("\nCheck inside the fridge ",answer5)
                elif answer5 == "Salad":
                    print("\nCheck inside the freezer for the ",answer5)
                else:
                    print("\nSorry!!, we don\'t have your request")
                    answer6 = input("\nWould you like to pick another options? Yes/No ")
                    if answer6 == "Yes":
                        print(input("\nWhat do you care for? "))
                    else:
                        print("\nSorry!!, we don\'t have your request")
            else:
                print("\nGo back to the parlour")
        else:
            print("\nYou missed the road")
    else:
        print("\nYou may have your seat")
else:
    print("\nIt is nice seeing you around goodbye")






