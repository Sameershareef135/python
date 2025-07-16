# while loop executes when while some condition remains true

#name = input("Enter your name: ")

#while name == "":
#    print("You did not enter a name")
#    name = input("Enter your name: ") #removing this line will lead to infinit no.of executions of while loop

#print(f"Hello {name}")

# Example 2
#food = input("Enter your favourite food (press q for quit): ")

#while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter another favourite food: ")
#print("bye")

# Example 3
#age = int(input("Enter your age: "))

#while age<0:
#    #print("Age cannot be negative")
#    age = int(input("Enter your age: "))
#print(f"You are {age} years old")

# Examole 4
num = int(input("Enter a number between 1-10: "))

while num < 1 or num>10 :
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"Your number is {num}")