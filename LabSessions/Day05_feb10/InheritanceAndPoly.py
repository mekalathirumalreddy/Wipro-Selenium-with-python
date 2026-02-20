#Lab 1: Method Overriding with Inheritance Create a base class Employee with a method calculate_salary(). Create a subclass Manager that overrides calculate_salary() and adds a bonus. Demonstrate runtime polymorphism using parent class reference.

class Employee:
    def calculate_salary(self):
        return 3000
class Manager:
    def calculate_salary(self):
        return 3000+2000
emp=Employee()
mgr=Manager()
print(emp.calculate_salary())
print(mgr.calculate_salary())

#2 Create classes Dog, Cat, and Cow with method speak().

class Dog:
    def Speak(self):
        print("Dog Bark")
class Cat:
    def Speak(self):
        print("Cat Meows")
class Cow:
    def Speak(self):
        print("Cow Moos")
def animal_sound(animal):
    animal.Speak()
animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())


#3. Create Vehicle → Car → ElectricCar.
#Override method fuel_type() in each class.


class Vehicle:
    def Fuel_type(self):
        print("Uses Fuel")
class Car(Vehicle):
    def Fuel_type(self):
        print("Uses petrol or diesel")
class ElectricCar(Vehicle):
    def Fuel_type(selfs):
        print("Uses Electicity")

V=Vehicle()
C=Car()
E=ElectricCar()

V.Fuel_type()
C.Fuel_type()
E.Fuel_type()

#4 Create a BankAccount class.
#Overload + to add balances and > to compare balances.

class BankAccount:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value + other.value

    def __gt__(self, other):
        return self.value > other.value

a=BankAccount(50000)
a1=BankAccount(400)

print(a+a1)
print(a>a1)

#5 Create classes A, B, C, and D (diamond structure).
# Override the same method in B and C.
# Observe MRO.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()
print(D.mro())


#7 Create Calculator with divide().
# Create SafeCalculator that handles divide-by-zero.

class Calculator:
    def divide(self,a,b):
        return a/b
class SafeCalculator(Calculator):
    def divide (self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "cannot divide by zero"
cal=SafeCalculator()
print(cal.divide(10,0))

#8 Create base class Payment.
# Create CreditCard, UPI, and NetBanking.
# Use one function to process payments.

class Payment:
    def pay(self, amount):
        print("Payment processing")

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")

def process_payment(payment, amount):
    payment.pay(amount)

process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
process_payment(NetBanking(), 2000)
