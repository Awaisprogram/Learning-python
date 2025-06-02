# Inheritance

# Creating a  new class using an existing class

# Types of Inheritance

# 1. Single Inheritance

class Employee:
  company = "Karachi"

  def showSelf(self):
    print(f"The name of Employee is {self.name} and his salary is {self.salary}")


"""
class Programmer:
  company = "Karachi University"

  def showSelf(self):
    print(f"The name of Programmer is {self.name} and his salary is {self.salary}")
   
  def showLanguage(self):
    print(f"The name of Programmer is {self.name} and his salary is {self.salary}")
"""

# Inherited Class

class Programmer(Employee):
  company = "Karachi University"

  def showLanguage(self):
    print(f"The name of Programmer is {self.name} and his salary is {self.salary}")    

a = Employee()
b = Programmer()

print(a.company, b.company)

# 2. Multiple Inheritance

class Employee:
  company = "Karachi"
  name = "Awais"
  def showSelf(self):
    print(f"The name of Employee is {self.name} and his company is {self.company}\n")
 

 
class Code:
  Language = "Python"

  def showLanguage(self):
    print(f"The Language is {self.Language}\n")

# Inherited Class

class Programmer(Employee,Code):
  company = "Karachi University"
  salary = 220000
  def printLanguage(self):
    print(f"The company of Programmer is {self.company} and his salary is {self.salary}\n")    

a = Employee()
b = Programmer()
b.showSelf()
b.showLanguage()
b.printLanguage()


# 3. Multilevel Inheritance

class Employee:
  a = 1


class Programmer(Employee):
  b = 2


class Manager(Programmer):
  c = 3

o = Employee()

print(o.a) # Print the attrribute
# print(o.b) # shows the error the attrribute cuz b dont exist

o = Programmer()

print(o.a ,o.b) 

o = Manager()

print(o.a ,o.b, o.c) 



# Constructor 


class Employee:
  def __init__(self):
    print("Constructor of Employee")
  a = 1


class Programmer(Employee):
  def __init__(self):
    print("Constructor of Programmer")
  b = 2


class Manager(Programmer):
  def __init__(self):
    super().__init__()
    print("Constructor of Manager")
  c = 3

o = Employee()

print(o.a) # Print the attrribute
# print(o.b) # shows the error the attrribute cuz b dont exist

o = Programmer()

print(o.a ,o.b) 

o = Manager()

print(o.a ,o.b, o.c) 

# Class Method

class Employee:
  a = 1
  @classmethod
  def show(cls):
    print(f"The value of class attribute is {cls.a}")

e = Employee()
e.a = 45

e.show()


# Property Decorator

class Employee:
  a = 1
  @classmethod
  def show(cls):
    print(f"The value of class attribute is {cls.a}")
  @property
  def name(self):
    return f"{self.fname} {self.lname}"
  @name.setter
  def name(self, value):
       self.fname = value.split(" ")[0]
       self.lname = value.split(" ")[1]  

       
      

e = Employee()
e.a = 45

e.name = "Awais Mehmood"
print(e.fname, e.lname)

e.show()

# Operators overloading

class Number:
  def __init__(self, n):
    self.n = n
  
  def __add__(self, num):
    return self.n + num.n

n = Number(1)
m = Number(2)

print(n+m)