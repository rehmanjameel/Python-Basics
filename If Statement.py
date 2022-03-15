temperature = 0

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: #(20, 30]
    print("It's a nice day")
elif temperature > 10: #(10, 20]
    print("It's a bit cold")
else:
    print("It's cold")

# print("Temperature is normal")

# Exercise
weight = float(input("Weight: "))
unit = input("Enter unit as K(g) or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in (L)bs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in (K)g: " + str(converted))
else:
    print("Invalid Unit!")
