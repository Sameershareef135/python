# COMPOUND INTEREST CALCULATOR

principal=0 
rate= 0
time = 0
n = 0

# formula A= P(1+r/n)^nt

while principal<= 0:
    principal = float(input("Enter your principal amount: "))
    if principal <=0 :
        print("Principal amount can't be less than or equal to 0")
    else : 
        break
while True:
    rate = float(input("Enter the rate of interest: ")) 
    rate = rate/100
    if rate <=0:
        print("Rate of interest can't be less than or equal to 0")
    else : 
        break
while time <= 0 :
    time = float(input("Enter the amount of time: "))
    if time <= 0:
        print("Time can't be less than or equal to 0")
    else : 
        break
while True:
    n = int(input("Enter the no.of times you want the interest to be applied(n): "))
    if n<=0:
        print("'n' can't be less than or equal to  0")
    else : 
        break
# two ways to go with while loop using "while true" and "while principal <=0"
# "while true" executes indefinitely and needs "break" statement to get out of loop

#print(principal)
#print(rate)
#print(time)
#print(n)

total = principal * pow((1+rate/n),n * time)

print(f"Your total amount is {total:.2f} after {time} year/s")