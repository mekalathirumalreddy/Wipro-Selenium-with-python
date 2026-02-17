# BASIC OOPS CONCEPTS / CLASS & OBJECTS
#Create a Car class with attributes brand, model, price.
print("======BASIC OOPS CONCEPTS========")

class car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
c1=car("Bmw","x5",5000000)
c2=car("audi","x",6000000)
print(c1.brand)
print(c2.price)
print(c1.model)


#Create a Student class with method get_grade() based on marks.

class Student:
    def __init__(self,marks):
        self.marks=marks
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"
c1=Student(82)
print(c1.get_grade())

#Create a BankAccount class with deposit() and withdraw() methods.

class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print("Not enough money")
c1=BankAccount(1000)
c1.deposit(500)
c1.withdraw(300)
print(c1.balance)

#Write a class Employee that initializes name, id, salary using __init__.
class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

#Create a class that counts how many objects are created.

class counter:
    count=0 #class variable
    def __init__(self):
        counter.count+=1
a=counter()
b=counter()
c=counter()
print(counter.count)

#Create a class Company with a class variable company_name.
class Company:
    company_name = "Wipro"

#Implement a static method to validate email format.

import re

class validator:
    @staticmethod
    def validate_email(email):
        return "@" in email
a1=validator.validate_email("vtu12345@gmail.com")
print(a1)

# ============INHERITANCE===================
print("=============INHERITANCE==============")

# PARENT -----> CHILD

#Create a base class Vehicle and derived class Bike.
#single inheritance
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Bike(Vehicle):
    pass
Bike().start()

#Create Person → Employee → Manager (multilevel inheritance).

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

a1=Manager("varun",20,6)
print(a1.name)
print(a1.emp_id)
print(a1.team_size)

#Override a method in child class and call parent method using super().
class Parent:
    def show(self):
        print("parent method")
class Child(Parent):
    def show(self):
        print("Child Method")

c1=Child()
c1.show()

#ENCAPSULATION
print("======ENCAPSULATION======")

#Create a class BankAccount with private balance.

class BankAccount:
    def __init__(self):
        self.__balance=0

#Use getter and setter methods to update balance safely.

class BankAccount1:
    def __init__(self):
        self.__balance=0

    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance+=amount
acc=BankAccount1()
acc.set_balance(5000)
print(acc.get_balance())

#Prevent negative salary using property decorators.
class Employee:
    def __init__(self,salary):
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value < 0:
            print("Invalid salary")
        else:
            self._salary=value
e = Employee(15000)

print(e.salary)     # get
e.salary = 25000    # set
print(e.salary)

e.salary = -1000    # invalid
print(e.salary)
#POLYMORPHISM

print("====POLYMORPHISM======")

#Create a Shape class with method area(). Implement Circle and Rectangle.
class Shape:
    def area(self):
        print("Area not defined")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
c=Circle(5)
r=Rectangle(4,6)
print(c.area())
print(r.area())

#Demonstrate method overloading using default arguments.
class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
c=calculator()
print(c.add(5))
print(c.add(5,10,20))
print(c.add(10,30))

#Demonstrate operator overloading (__add__).
class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


#Create Engine class and use it inside Car class.
print("============")
class Engine:
    def start(self):
        print("engine started")
class Car:
    def __init__(self):
        self.engine=Engine()
    def start(self):
        self.engine.start()
c=Engine()
c.start()

#Create Team class that contains multiple Player objects.
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)
team = Team()

team.add_player(Player("Virat"))
team.add_player(Player("Rohit"))

for p in team.players:
    print(p.name)
