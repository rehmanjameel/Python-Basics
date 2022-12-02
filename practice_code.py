print("Welcome to the Love Calculator")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combine_names = name1 + name2
name_lower_case = combine_names.lower()

t = name_lower_case.count("t")
r = name_lower_case.count("r")
u = name_lower_case.count("u")
e = name_lower_case.count("e")

true = t + r + u + e

l = name_lower_case.count("l")
o = name_lower_case.count("o")
v = name_lower_case.count("v")
e = name_lower_case.count("e")

love = l + o + v + e

true_love_score = int(str(true) + str(love))

print(f"{true_love_score}%")

if (true_love_score < 10) or (true_love_score > 90):
    print(f"Your love score is {true_love_score}, you go together like coke and mentos.")
elif (true_love_score >= 40) and (true_love_score <= 50):
    print(f"Your love score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}")
