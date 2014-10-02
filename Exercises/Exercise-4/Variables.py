pennies = 10
quarters = 15
dimes = 33
money = (pennies * 0.01) + (dimes * 0.10) + (quarters * 0.25) # Gotta use them floating point numbers
soda = 1.75
water = 1.0

# Print stuff or something i guess
print "In my pocket I have ", quarters, " quarters, ", dimes, " dimes, and ", pennies, " pennies."
print "In total I have ", money, "."
print "If I were to buy a soda I'd have ", money - soda, "."
print "However, if I buy two waters I'll have ", money - (water * 2), "."
print "I'll take the water"