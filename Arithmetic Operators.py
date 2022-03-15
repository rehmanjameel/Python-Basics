print(10+3)
print(10-3)
print(10*3)
# single slash returns floating point
print(10/3)
# double slash returns the whole numbers
print(10//3)
# modulus returns the reminder
print(10%3)

# exponent operator '**' indicate the power of number
print(10 ** 3)

# Assignment operators
x = 10
x = x+3
#or
x += 3
x *= 3

print(x)

# Operator precedence
x = 10 + 3 * 2
x1 = (10 + 3) * 2

print(x)
print(x1)

# Comparison Operator
x = 3 > 2 #this expression returns boolean
print(3 < 2)
x2 = 3 ==2
print(x2)

price = 25
print(price > 10 and price < 30)
print(price > 10 or price == 30)
print(not price == 30)