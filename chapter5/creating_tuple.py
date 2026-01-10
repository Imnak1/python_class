#!/usr/bin/python3

tuple2 = (1, 2, 3, 4, 5 )


#Accessing values in a tuple

continents = ("Asia", "Africa", "Americas", "Europe", "Australia")

print ("continents[0]:", continents[0])

print ("continents[2:]", continents[2:])

print ("continents[:-3]", continents[:-3])

#Updating a tuple
continents = ("Asia", "Africa", "Americas", "Europe", "Australia")

continents2 = ("Antarctica",)

all_continents = continents + continents2

print (all_continents)

print("there are", len(all_continents), "continents")
