class Animals:
     isAlive = True

     def eat(self):
          print("This animal is eating")

     def sleep(self):
          print("This animal is sleeping")

class Rabbit(Animals):

     def run(self):
          print("This rabbit is running")

class Fish(Animals):

     def swim(self):
          print("This fish is swimming")

class Hawk(Animals):

     def fly(self):
          print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.isAlive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

# Supper function

# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

import Classes
print(__name__)
print(Classes.__name__)