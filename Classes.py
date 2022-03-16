se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]

class SoftwareEngineer:
    # Class attribute can be access by class name or class instance
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes can be access only by instance
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)