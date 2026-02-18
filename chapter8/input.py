"""
k = [1]
print(k)

#exercise on fstring
name = "John" 
age = 21 
print ("My name is {} and I am {} years old.".format(name,age)) 

#String formatting with arguments
print("Hello. My name is {name}, and I am a {occupation}.".format(occupation = "programmer", name = "John"))


#exercise on input 

#name = str(input("Enter your name: ")) 

#age = int(input("How old are you?: ")) 

#sex = str(input("Enter your gender M or F: ")) 

#location = str(input("Which city do you live in: ")) 

if sex == "M" or "m": 
    gender = "male" 
elif sex == "F" or "f": 
    gender = "female" 
else: 
    gender = "invalid" 

print ("{}, you are a {} old {} from {}.".format(name, age, gender, location))
print (f"{name}, you are a {age} old {gender} from {location}.")
"""
"""
# Opening of File

f = open("poem.txt", "r") 
poem = f.read(); 
print(poem) 
"""

"""
file = open("myfile.txt", "w") 

file.write("The purple cow poem is a short nonsense poem first published in 1895 written by American writer Gelett Burgess"); 
file.close() 
"""

with  open("sample.txt","w") as file:
    file.write("i love python")


with open ("sample.txt", "a+") as file:
    file.write("\nI am a programmer")

with open("sample.txt", "r") as file:
    text = file.readline()
    #print(text)
    textt = file.readlines()
    print(textt)   

#module import