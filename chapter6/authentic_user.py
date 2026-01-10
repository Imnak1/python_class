#!/usr/bin/python3


#authetication code


users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "userpass", "role": "user"},
    "guest": {"password": "guest", "role": "guest"}
}

# Get user input
username = input("\nEnter username: ")
password = input("\nEnter password: ")
role = input("\nEnter role: ")

#Check the user membership

if username in users:
    print("\nYou are welcome", username)
    
    #confirmation of password
    if users["admin"]["password"] == password:
        print("\nYou have succesfully login", username)
        if users["admin"]["role"] == role:
            print("\nYou have full access", username)
        else:
            print("\nunassigned role")
    elif users["user1"]["password"] == password:
        print("\nYou have succesfully login", username)
        if users["user1"]["role"] == role:
            print("\nYou have limited access", username)
        else:
            print("\nunassigned role")
    elif users["guest"]["password"] == password:
        print("\nYou have succesfully login", username)
        if users["guest"]["role"] == role:
            print("\nYou have read only access", username)
        else:
            print("\naccess denied")
    else:
        print("\nInvalid password")


