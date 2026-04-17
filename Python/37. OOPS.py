# object = a 'bundle' of related attributes (Variables) and methods (functions)

# class = (blueprint) used to design the structure and layout of an object
# class is needed to create many objects


class Car:
    def __init__(self, model, year, color, for_sale):  # Constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving the {self.color} {self.model}!")

    def stop(self):
        print(f"You stopped the {self.color} {self.model}!")

    def describe(self):
        print(f"This car is a {self.color} {self.model}.")


car1 = Car("Mustang", 2026, "Black", False)

print(car1)  # will print memory address
print(car1.model)  # to print model
print(car1.color)
print(car1.year)
print(car1.for_sale)
car1.describe()
car1.drive()
car1.stop()

car2 = Car("Mercedes CLA", 2024, "Red", True)

print(car2)  # will print memory address
print(car2.model)  # to print model
print(car2.color)
print(car2.year)
print(car2.for_sale)
car2.drive()
car2.stop()


# for better organization we can place the class in another python file and then import it


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class variables - shared amongst all instances of a class, defined outside the constructor, allow you to share data among all objects created from that class


class student:

    class_year = 2028  # Class variable, it will be common for all objects
    num_students = 0

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        student.num_students += 1


student1 = student("Harshit Taneja", 826)
student2 = student("Prisha Acharya", 190)
student3 = student("Mehakdeep Singh", 827)
student4 = student("Vandit Gupta", 315)

print(student1.name)
print(student1.rollno)
print(student.class_year)  # Calling class variable


print(
    f"My Graduating class of {student.class_year} has {student.num_students} students - "
)
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Inheritence - Allows a class to inherit attributes and methods from another class


class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):  # the class Dog inherits everything from parent class Animal
    def speak(self):
        print("WOOF!!")


class Cat(Animal):  # the class Cat inherits everything from parent class Animal
    def speak(self):
        print("MEOW!!")


dog = Dog("Maggi", True)
cat = Cat("Jerry", True)

print(dog.name, dog.is_alive)
dog.eat()
dog.speak()
dog.sleep()
dog.speak()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multiple Inheritence = child inherits from multiple parents (C(A,B))
# Multilevel = inherit from a parent which inherits from another parent (C<B<A)
class organism:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class prey(organism):
    def flee(self):
        print(f"{self.name} is fleeing")


class predator(organism):
    def hunt(self):
        print(f"{self.name} is hunting")


class rabbit(prey):
    pass


class hawk(predator):
    pass


class fish(prey, predator):
    pass


rabbit = rabbit("Bugs")
hawk = hawk("Tony")
fish = fish("Nemo")

rabbit.flee()
rabbit.eat()
rabbit.sleep()


fish.hunt()
fish.eat()
fish.sleep()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# super() - function used in a child class to call methods from a parent class(superclass)
# Allows you to extend the functionality of the inherited methods
# to reuse constructor of parent class


class shapes:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled


class circle(shapes):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius


class square(shapes):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width


class triangle(shapes):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height


circle = circle("Red", True, 10)
square = square("Blue", False, 4)

print("Square")
print(f"Filled = {square.filled}")
print(f"Width = {square.width} units")


print("Circle")
print(f"Filled = {circle.filled}")
print(f"Radius = {circle.radius} units")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Polymorphism - "to have many forms or faces"
# Two ways :
# 1. Inheritence = Object is treated of the same type as a parent class
# 2. Duck Typing = Object must have necessary attributes/methods

# Inheritence

from abc import ABC, abstractmethod  # to work with abstract classes we import this


class shape:
    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# circle = circle()  # A circle is a shape and a circle
# square = square()


class Pizza(circle):  # Pizza is pizza, a circle and a shape
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius


shapes = [circle(4), square(5), triangle(6, 7), Pizza("Cheese", 15)]


for shape in shapes:
    print(f"{shape.area()} cm")


# Duck Typing = Object must have necessary attributes/methods
#  If it looks like a duck and quacks like a duck, it must be aa duck


class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class car:  # car is not an animal but due to its speak function it will be considered as an animal
    alive = False

    def speak(self):
        print("Honk!")


animals = [Dog(), Cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


class car:
    def speak(self):
        print("Honk!")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Static Methods - A method that belongs to a class rather than any object from that class(instance)
# Instance Methods - Best for operations on instances of the class(objects)
# Static Methods - Best for utility functions that do not need access to class data


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        print(f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid = ["Manager", "Cook", "Janitor", "Cashier"]
        return position in valid


print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Driver"))

emp1 = Employee("Harshit", "Manager")
emp1.get_info()
emp2 = Employee("HogRider", "Cook")
emp2.get_info()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class Methods - Allow operations related to the class itself
# Take (cls) as the first parameter which represents the class itself


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        print(f"{self.name}, GPA = {self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total number of students = {cls.count}"
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count:.2f}"


print(Student.get_count())
s1 = Student("Harshit Taneja", 9.55)
s2 = Student("Mehakdeep Singh", 9.27)
s3 = Student("Vandit", 8.76)
s1.get_info()
s2.get_info()
s3.get_info()
print(Student.get_count())
print(Student.get_avg_gpa())


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Magic Methods - Dunder Methods (double underscore) __init__, __str__, __eq__
# They are automatically called by mant of pythons built-in operations
# They allow developers to define or customize the behaviour of objects


class book:

    def __init__(
        self, title, author, pages
    ):  # __init__ used to create constructor of class
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # To print string representation of object
        return f"'{self.title}' by {self.author}"

    def __eq__(self, value):  # to check if objects are equal
        return self.title == value.title and self.author == value.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author


b1 = book("Hobbit", "J.R.R Tolkien", 310)
b2 = book("The count of monte cristo", "Alexandre Dumas", 421)
b3 = book("Angles & Demons", "Dan Brown", 562)
b4 = book("Angles & Demons", "Dan Brown", 635)

print(b1)  # __str__
print(b2)  # __str__
print(b3)  # __str__
print(b4 == b3)  # __eq__
print(b1 < b2)  # __lt__
print(b2 > b3)  # __gt__
print(b2 + b3)  # __add__
print("Dan" in b3)  # __contains__
print("Rowling" in b3)  # __contains__

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# @property = decorator used to define a methods as a property (can be accessed like an attribute)
# Benefit : add additional logic when read, write or delete attributes
# Gives you getter, setter and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width  # self._width means that this attribute is private and cannot be accessed outside the class
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


r1 = Rectangle(3, 4)
print(r1.width)
print(r1.height)
r1.width = 12
r1.height = 15
print(r1.width)
print(r1.height)
del r1.width
del r1.height

