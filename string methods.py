name = input("Enter your name: ")
#phone_no = input("Enter your phone number: ")

#length (starts from 1 and includes spaces)
#result = len(name)

#find (start from 0)
#result = name.find("a")
#result = name.rfind("o")
#result = name.find("O")

#capitalize 
#name = name.capitalize()

#upper
#name = name.upper()

#lower
#name = name.lower()

# isdigit
#result = name.isdigit()

# isalpha
#result = name.isalpha()

#count
#result = phone_no.count("-")

#print(result)

#replace
#phone_no = phone_no.replace("-","")

#print(phone_no)

# to get or remember all string functions
#print(help(str))

# EXERCISE
#validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username)>12:
    print("Your username can't exceed more than 12 characters")
elif not username.find(" ") == -1:
    print("your username must not contain spaces")
elif not username.isalpha():
    print("your username must not contain digits") 
else :
    print(f"welcome {username}")