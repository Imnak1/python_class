#!/usr/bin/python3

#creating of sets
# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using set() function
my_set2 = set([1, 2, 6, 7, 8])

print(my_set)

print(my_set2)

print(type(my_set))


#Adding element

my_set.add(6)

print(my_set)

my_set.update(my_set2)

print(my_set)

print(3 in my_set)

print(7 in my_set)



#Sets in union operation

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # {1, 2, 3, 4, 5}

print(A.union(B))  # Same result

#Intersection (& or intersection())

#Finds common elements:

print(A & B)  # {3}


print(A.intersection(B))


#Sets differences

print("The result is", A - B)  # {1, 2}
print(A.difference(B))  # Same result

#Symmetric Difference (^ or symmetric_difference())

#Elements that are in one set but not both:

print(A ^ B)  # {1, 2, 4, 5}
#print(A.symmetric_difference(B)) 




#Set comaprison

X = {1, 2}
Y = {1, 2, 3, 4}

print(X < Y)  # True (X is a proper subset of Y)
#print(X.issubset(Y))  # True
#print(Y.issuperset(X))  # True


#Set Comprehension

#You can create sets using comprehension:

squared = {x**2 for x in range(5)}
print(squared)  # {0, 1, 4, 9, 16}

b = []
for x in range(5):
    b.append(x**2)
    x = x + 1

print(b)


# Operation with frozensets


fs1 = frozenset({1, 2, 3, 4})
fs2 = frozenset({3, 4, 5, 6})
    
print(fs1 | fs2)
print(fs1 & fs2)





