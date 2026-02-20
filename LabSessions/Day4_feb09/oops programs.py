#1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
#2.Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
#3.Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
#4.Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class
#5.Write a python program to create  a Vehicle class without any variables and methods

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
c = Circle(5)
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())


from datetime import date

class Person:
    def __init__(self, name, country, year, month, day):
        self.name = name
        self.country = country
        self.dob = date(year, month, day)

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age


# Example usage
p = Person("Reddy", "India", 2002, 5, 10)
print("Name:", p.name)
print("Age:", p.age())


import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Example usage
sq = Square(4)
print("Square Area:", sq.area())
print("Square Perimeter:", sq.perimeter())


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)


class Bus(Vehicle):
    pass


# Example usage
b = Bus("Volvo", 80)
b.show_details()


class Vehicle:
    pass


# Example usage
v = Vehicle()
print("Vehicle object created")
