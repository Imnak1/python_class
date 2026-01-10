#!/usr/bin/python3

#function to create register
users = {}

def register():

    username = input("\nEnter your username: ")
    if username in users:
        print("\nusername already exist, change username: ")
        return
    password = input("\nEnter your password: ")
    role = input("\nEnter your role (admin/user/guest): ").lower()
    print("\nMy role is", role)

    if role not in ['admin', 'user', 'guest']:
        print('\nInvalid role')
        role = ('guest')
    users[username] = {"password": password, "role":role}
    print("\n",users)
    print("Registration is successful")


#register()

def login():
    username  =input("\nEnter your username: ")
    password = input("\nEnter your password: ")
    
    if username in users:
        if users[username]["password"] == password:
            print("You've successfully login")

            if users[username]["role"] == "admin":
                print("welcome admin! you have full access")
            elif users[username]["role"] == "user":
                print("welcome user! you have limited access")
            else:
                print("welcome guest! you have view only access")

        else:
            print("incorrect password")

    else:
        print("username not found register first")

#login()


# Main function to provide menu options
def main():
    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()

    
