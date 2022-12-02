"""error code TypeError: can only concatenate str (not "int") to str"""
# num_char = len(input("What is your name?"))
# print("Your name has" + num_char + " character.")

"""Correct code"""
# num_char = len(input("What is your name?"))
#
# new_num_char = str(num_char)
#
# print("Your name has " + new_num_char + " characters.")

"""Type checking"""
# a = 123
# b = str(123)
# c = float(123)
# print(type(a))
# print(type(b))
# print(type(c))

"""Exercise: Add two digit numbers in ine input"""
# two_digit_number = input("Enter two digit number: ")
# add_numbers = float(two_digit_number[0]) + float(two_digit_number[1])
# print(add_numbers)

"""BMI calculator"""
# height = input("Enter your height in meters: ")
# weight = input("Enter your weight in kg: ")
# bmi = int(weight) / float(height) ** 2
# result = int(bmi)
# print(result)

"""round function"""
# print(round(8/3, 2))

"""f-string"""
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

"""Find age in weeks"""
# age = int(input("Enter your current age: "))
#
# years_remaining = 90 - age
#
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# print(f"You have {years_remaining} years, {months_remaining} months, "
#       f"{weeks_remaining} weeks and, {days_remaining} days remaining.")
#
# a = int("5") / int(2.7)
# print(a)

# print("Hello, welcome to coffee shop!")
#
# name = input("What is your name? \n")
#
# print("Hello " + name + " thank you so much for coming in today.\n\n")
#
# menu = "Black Coffee, Espresso, Latte, Cappucino"
#
# order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")
#
# price = 8
#
# quantity = input("How much coffees would you like? \n")
#
# total = price * int(quantity)
#
# print("Sounds good " + ", we'll have that " + order + " ready for you in a moment. "
#                                                       "\nYour total price is ", total)


import random

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# num_items = len(names)
# random_name = random.randint(0, num_items - 1)
# chosen_person = names[random_name]
# random_name = random.choice(names)
# print(f"{random_name} is going to buy the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][1])
