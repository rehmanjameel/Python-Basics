# While loop
i = 1
while i <= 1_0: #1_0 means this number is 10
    print(i * "*")
    i += 1

# For loops
# shorter and easy to use than while loop
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# on the other hand while be like
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# range() function
range_number = range(5) # this function will print the numbers of range 0 to 5 excluding 5
for number in range_number:
    print(number)
# We can provide the starting and ending number in range
# we can add the steps to jump on more than 1 number be like 5, 7, 9
start_endRange = range(5, 10, 2)
for number in start_endRange:
    print(number)

# we can use the range function with in the for loop instead of using object
for num in range(5):
    print(num)
