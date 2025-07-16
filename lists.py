# collection variables are single variables used to store multiple values
# list, set ,tuples and dictionaries are also known as collection variables
# collection variables are able to store multiplie values

# list [] are ordered and their values can be changed/mutable. it allows duplicate values

fruits = ["apple", "orange", "banana", "mango"]
#print(dir(fruits))

# index in list starts from 0
#print(fruits[1]) 
#print(fruits[1:])
#print(fruits[:3]) 
#print(fruits[::2])
#print(fruits[::-1]) 
#print(len(fruits))
#print("apple" in fruits)
#print("berry" in fruits) # berry does not exist in fruits list/variable so O/P will be false

#for fruit in fruits:
#   print(fruit)

# CHANGE VALUES IN LIST
#fruits[0] = "berry" # changes apple to berry

#fruits.append("berry") # adds berry to the list
#fruits.remove("apple") # removes apple from the list
#fruits.insert(0,"mosaambi") # insert any value at any index
#fruits.sort() # sorts in ascending/alphabatical order
#fruits.reverse() # reverses the list in the written/given order
#fruits.clear() #clears the list
#print(fruits.index("mango")) # returns the index number
print(fruits.count("apple")) # counts the number of values present in the list

print(fruits)