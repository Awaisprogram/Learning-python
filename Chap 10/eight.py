# Object oriented program (OOPS)

# Basic class

class Employee: #noun | class 
  #adjective | attribute
  language = "Python"
  salary = 100000


Awais = Employee #verb | Class attribute
Awais.name = "Awais" 
print(Awais.name, Awais.language, Awais.salary)

Waleed = Employee
Waleed.name = "Waleed" #instance attribute
print(Waleed.name, Waleed.language, Waleed.salary)

# Here name is instance attribue and salary and language are class attributes as ther directly belong to the class


#########################################

# Instance vs Class Attributes


class Employee: 
  
  language = "Python"
  salary = 100000


Awais = Employee #verb | Class attribute
Awais.language = "JavaScript" #instance attribute
print(Awais.language, Awais.salary)

#########################################

#   Self Parameter


class Employee: 
  
  language = "Python"
  salary = 100000

  def greet(self):
    print("Good Morning")

  def getInfo(self):
    print(f"The language is {self.language} and the salary is {self.salary}")

  
Awais = Employee() #verb | Class attribute
Awais.language = "JavaScript" #instance attribute
print(Awais.language, Awais.salary)
Awais.greet()
Awais.getInfo()


#########################################

#   Static Method

class Employee: 
  
  language = "Python"
  salary = 100000

  @staticmethod
  def greet():
    print("Good Morning")

  def getInfo(self):
    print(f"The language is {self.language} and the salary is {self.salary}")

  
Awais = Employee() #verb | Class attribute
Awais.language = "JavaScript" #instance attribute
print(Awais.language, Awais.salary)
Employee.greet()
Awais.getInfo()

#########################################

#   INIT Constructor


class Employee: 
  
  language = "Python"
  salary = 100000

  def __init__(self, name, language,salary): #dunder method which is automaicaly called
    self.name = name
    self.language = language
    self.salary = salary
    

    print(f"I am creating an objct")

  @staticmethod
  def greet():
    print("Good Morning")

  def getInfo(self):
    print(f"The language is {self.language} and the salary is {self.salary}")

  
Awais = Employee("Awais", 12000 , "Python ") 
print(Awais.name , Awais.salary,Awais.language)
