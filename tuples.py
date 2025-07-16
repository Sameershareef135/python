# collection variables are single variables used to store multiple values
# list, set ,tuples and dictionaries are also known as collection variables
# collection variables are able to store multiplie values


# tuples () are ordered and unchangeable/immutable. allows duplicate. it is faster

fruits = ("apple", "orange", "banana", "mango")

#print(type(fruits))
#print(dir(fruits))
#print(help(fruits))

print(len(fruits))
print("berry" in fruits)

print(fruits.index("apple"))
print(fruits.count("apple"))

for fruit in fruits:
   print(fruit)