#!/usr/bin/python3
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
yearlist = [2017, "Two Thousand and Seventeen", "XXVII", 20.17]
favorites = ["a", "x", "i", "xx"]
print (weekdays)
print(weekdays[0])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
"Sep", "Oct", "Nov", "Dec"]

print ("The first month is", months[0])
print ("The 5th to 9th months are", months[4:9])
print ("The second last month is", months[-2])
print (months[6:], "make up the last half of the year")

subjects = ["Math", "Physics", "Chemistry"]

print ("List of subjects:", subjects)

subjects[2] = "Biology"

print ("New list of subjects: ", subjects)

subjects.extend(["Geography", "Law", "Accounting"])
print(subjects)


subjects = ["Math", "Physics", "Chemistry", "Biology", "History"]
print ("List of subjects:", subjects)

del subjects[2]
print ("New list of subjects after del: ", subjects)

subjects.remove("Physics")
print (subjects)
