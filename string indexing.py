#accessing elements of a sequence using [](indexing operator) 
#  [start:end:step]

credit_number = "1234-4567-3123-8792"

#print(credit_number[0])
#print(credit_number[1])
#print(credit_number[2])
#print(credit_number[1:])
#print(credit_number[:4])
#print(credit_number[0:4])
#print(credit_number[1:6])
#print(credit_number[-3])

#print(credit_number[::2])
#print(credit_number[::3])
#print(credit_number[1:6:2])


# EXERCISE
# LAST 4 NUMBERS OF CREDIT NUMBER

last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")

# EXERCISE 2
# reverse the string of credit_number

#credit_number = credit_number[::-1]
print(last_digits)