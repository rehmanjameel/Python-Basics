# Tuples are immutable we cannot change or reassign the values'
# parenthesis () are used to define the tuple
tupleNumbers = (1, 2, 3, 4, 3)
# tupleNumbers[0] = 10  ## this line of code will generate the error
count = tupleNumbers.count(3) # this method returns the number of occurrence of element
indexs = tupleNumbers.index(4) # this method shows the index of element
print(tupleNumbers)
print(count)
print(indexs)