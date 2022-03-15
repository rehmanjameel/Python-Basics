# input a username
# Here we don't need to declare the datatype of variable
# name = input("What is your name? ")
# print("Hello " + name)

# Type Conversion
# Conversion from string to int
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
# Here is error in print as python cannot concatenate string with float
# print("Sum: " + sum)
# For this we need to cast float with str()
print("Sum: " + str(sum))