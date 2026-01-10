#!/usr/bin/python3


#For loop

numbers = [3, 9, 16, 7, 8, 2, 5, 4, 10] #List of numbers 

sumi  = 0 

#variable to store the sum
 
for val in numbers:
    #iterate over the list 
    sumi = sumi + val 
#print (f'The total value is ${sumi}')
#print("\nThe total value is", sumi)

#for loop for range() function
total = 0
for x in range(10,20,2):
    total = total + x
    #print (x, "\n")
#print ("The totals is:", total)

#for loop for else()
numbers = [0, 1, 3, 5, 6, 9, 10]
#for i in numbers:
      #print(i)
#else:
    #print("No more numbers to print.")


#while loops

x =  int(input("Enter a value for x: ")) 
sumi = 0 
i = 1 
while i <= x: 
     sumi = sumi + i 
     print (sumi) 
     i = i + 1 # update counter
     print(f'the value of i is {i}')
print ("The total sum is", sumi)




name  = ["yeye", "ayo", "ola", "ogo"]
count = 0
for x in name:
    count = count + 1
    print ('The name of my people', x)
    print(f'the name of the people are {x}')

print(f'the total number of people is {count}')


name = ['yeye','jao','funso']
count = 0
i = 1
while count < len(name):
    count = count + i
    print(f'the name of my people are {count}')
    i = i + 1

print(f'the total number of people {count}')

#while_loops

loops = int(input("Enter the number of times to loop: ")) 

counter = 0 
while counter < loops: 
      counter = counter + 1 
      print ("Iterations so far:", counter) 
else: 
       print("Maximum loops of", loops, "reached") 




