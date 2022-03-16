# Lists are mutable we can change them easily

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names)
print(names[0:3]) # This will exclude the index 3

#List methods

numbers = [1, 2, 3, 4, 5]
# add the number at the end of list
# like [1, 2, 3, 4, 5, 6]
numbers.append(6)

# To add the number in the centre or any other position of list use "insert"
numbers.insert(3, -1)

# We can remove the value from list
numbers.remove(3)

# We can remove the all values from list using clear
# numbers.clear()

print(numbers)

# We can check the value in list that it is present or not by returning boolean value
print(1 in numbers) # returns true as 1 is present

# We can find the length of list values
print(len(numbers))
