# Object oriented program pracitce
from random import randint


# simple object

class Food:
  name = "Biryani"
  price = 1200

d = Food()
print(d.name, d.price)

# Instace attribute

class Student:
  name = "Awais"
  number = 400

s = Student()
s.name = "Waleed" 
print(s.name,s.number)  

# Programmers

class Programmer():
  def __init__(self,name,salary,language):
    self.name = name
    self.salary = salary
    self.language = language

p = Programmer("Awais", 120000 , "Python")
print(p.name,p.language,p.salary)

# Calculator

class Calculator:
  def __init__(self , n):
    self.n = n

  def square(self):
    print(f"The sqaure of {self.n} is {self.n * self.n}")
  
  def cube(self):
    print(f"The cube of {self.n} is {self.n * self.n * self.n}")

  def squreRooot(self):
   print(f"The squreRooot of {self.n} is {self.n ** 1/2}")

cal = Calculator(4)
cal.square()
cal.cube()
cal.squreRooot()

# Checker

class Checker:
  a = 4
  print(a) # Print 4

check = Checker()
check.a = 0
print(check.a)  # Print 0
print(Checker.a) # Print 4

"""
This means the instance attribute does not change the class attribute and just instance attribute get priority over class attribute
"""

# Static Method


class Calculator:
  def __init__(self , n):
    self.n = n  

  def square(self):
    print(f"The sqaure of {self.n} is {self.n * self.n}")
  
  def cube(self):
    print(f"The cube of {self.n} is {self.n * self.n * self.n}")

  def squreRooot(self):
   print(f"The squreRooot of {self.n} is {self.n ** 1/2}")
  
  @staticmethod
  def greet():
    print("Hello user") 

cal = Calculator(4)
cal.greet()
cal.square()
cal.cube()
cal.squreRooot()

# 

class Train:

  def __init__(self, trainNo):
    self.trainNo = trainNo
 
  def ticket(self,From, to):
    print(f"The ticket of train {self.trainNo} is booked and  coming from {From} to {to} on time")

  def getStatus(self):
     print(f"Train{self.trainNo} is running on time ")

  
  def getFare(self,From, to):
   print(f"The ticket Fare of train  {self.trainNo} from {From} to {to} is {randint(222,555)}")

det = Train(123456)
det.ticket("Karachi", "Lahore")
det.getStatus()
det.getFare("Karachi", "Lahore")