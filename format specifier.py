# format specifiers - format a value based on what flags are inserted {value:flags}

price_1 = 3.1421
price_2 = -5533
price_3 = 903.55

# displays value in decimal/float number. 0,1,2 indicates the no.of points after a decimal
#print(f"Price 1 is ${price_1:.2f}")
#print(f"Price 2 is ${price_2:.1f}")
#print(f"Price 3 is ${price_3:.0f}")

# creates a space here 10 indicated number of spaces
#print(f"Price 1 is {price_1:10}")

# 0 padding
#print(f"Price 2 is {price_2:05}")
#print(f"Price 3 is {price_3:010}")

# left justify 
#print(f"Price 1 is {price_1:<10}")
#print(f"Price 2 is {price_2:<10}")
#print(f"Price 3 is {price_3:<10}")

# right justify 
#print(f"Price 1 is {price_1:>10}")
#print(f"Price 2 is {price_2:>10}")
#print(f"Price 3 is {price_3:>10}")

# center align
#print(f"Price 1 is {price_1:^10}")
#print(f"Price 2 is {price_2:^10}")
#print(f"Price 3 is {price_3:^10}")

# thousand separator
#print(f"Price 1 is {price_1:,}")
#print(f"Price 2 is {price_2:,}")
#print(f"Price 3 is {price_3:,}")

# show +/- sign
#print(f"Price 1 is {price_1:+}")
#print(f"Price 2 is {price_2:+}")
#print(f"Price 3 is {price_3:+}")

# mix and match 
print(f"Price 1 is {price_1:+010}")
print(f"Price 2 is {price_2:,.2f}")
print(f"Price 3 is {price_3:^+10.2f}")