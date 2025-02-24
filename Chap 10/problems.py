from random import randint

# 1
# Method 1

# class programmer:
#   company = "Microsoft"
#   name = "Awais"
#   language = "Python"
#   salary = "120000"

# Awais = programmer()
# print(Awais.name , Awais.language, Awais.salary)

# Method 2

# class programmer:
#   company = "Microsoft"
#   def __init__(self, name, salary, pin):
#     self.name = name
#     self.salary = salary
#     self.pin = pin    
    
# Awais = programmer("Awais", 120000, 50001 )
# print(Awais.company, Awais.name , Awais.salary, Awais.pin)

# 2

# class Calculator:
#   def __init__(self, n):
#     self.n = n
  
#   def square(self):
#     print(f"The square of {self.n} = {self.n*self.n}")

#   def cube(self):
#     print(f"The cube of {self.n} = {self.n*self.n*self.n}") 

#   def squareroot(self):
#     print(f"The squareroot of {self.n} = {self.n**1/2}")


# a = Calculator(int(input("Enter a number: ")))
# a.square()
# a.cube()
# a.squareroot()

# 3

# class Demo():
#   a = 4
# o = Demo()
# print(o.a)  # Print 4
# o.a = 0
# print(o.a)  # Print 0
# print(Demo.a) # Print 4

# It Does not change class attribute just priorotize instance attribute

# 4

# class Calculator:

#   @staticmethod
#   def greet():
#     print("Hello user")
#   def __init__(self, n):
#     self.n = n
  
#   def square(self):
#     print(f"The square of {self.n} = {self.n*self.n}")

#   def cube(self):
#     print(f"The cube of {self.n} = {self.n*self.n*self.n}") 

#   def squareroot(self):
#     print(f"The squareroot of {self.n} = {self.n**1/2}")


# a = Calculator(int(input("Enter a number: ")))
# a.greet()
# a.square()
# a.cube()
# a.squareroot()

# 5

class Train:

  def __init__(self,trainNo):
    self.trainNo = trainNo 

  def book(self,From, to):
    print(f"Ticket is booked in train no.{self.trainNo} from {From} to {to}")

  def getStatus(self):
   print(f"Train no.{self.trainNo} is running on time")

  def getFare(self,From, to):
    print(f"Ticket Fare in train no.{self.trainNo} from {From} to {to} is {randint(222,5555)}")

     
t = Train(123003)
t.book("Karachi" , "Lahore")  
t.getStatus()  
t.getFare("Karachi" , "Lahore")  