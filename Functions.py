from Classes import SoftwareEngineer

# lambda arguments : expression
# lambda function is a simple function that is used only once in code
add10 = lambda x: x + 10
print(add10(5))

se1 = SoftwareEngineer("AR", 23, "Junior", 5000)
print(se1.name)
se1.work()
se1.notWorking()