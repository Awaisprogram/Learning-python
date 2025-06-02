# ###### 1. OOPS 

# # creating class

# class Student:
#   name = "Awais"

# # creating object (instance)

# s1 = Student()

# print(s1.name)

# ####### 2. CONSTRUCTORS (__init__ function)

# class Student:
#   def __init__(self, fullname, marks) -> None:
#     print("Adding new student in Databse!")
#     self.name = fullname
#     self.marks = marks

# # creating object (instance)

# s1 = Student("Awais", 97)

# print(f"The marks of {s1.name} is {s1.marks}")

# s2 = Student("Ali",23)
# print(f"The marks of {s2.name} is {s2.marks}")

# ####### 3. CLASS & ATTRIBUTES

# class Student:
#   college_name = "ABC College"

#   def __init__(self, fullname) -> None:
#     print("Adding new student in Databse!")
#     self.name = fullname

# s2 = Student("Ali")
# print(s2.name)
# print(s2.college_name)

# ####### 4.   Methods

# class Student:
#   college_name = "ABC College"

#   def __init__(self, fullname, marks) -> None:
#     print("Adding new student in Databse!")
#     self.name = fullname
#     self.marks = marks

#   def welcome(self):
#     print(f"Welcome student {self.name}") 

#   def get_marks(self):
#     return self.marks   

# s2 = Student("Ali", 97)
# s2.welcome()
# print(s2.get_marks())


# #### 5. Static method

# class Student:
#   college_name = "ABC College"

#   def __init__(self, fullname, marks) -> None:
#     print("Adding new student in Databse!")
#     self.name = fullname
#     self.marks = marks

#   @staticmethod
#   def hello():
#     print("Hello")  

#   def welcome(self):
#     print(f"Welcome student {self.name}") 

#   def get_marks(self):
#     return self.marks   

# s2 = Student("Ali", 97)
# s2.welcome()
# print(s2.get_marks())
# s2.hello()

# ###### 6. PILLARS OF OOPs

# # (1) Abstraction

# class Car:
#   def __init__(self) -> None:
#    self.acc = False
#    self.brk = False
#    self.clutch = False

#   def start(self):
#     self.acc = False
#     self.brk = False
#     print("Car started...")

# car1 = Car()
# car1.start()    

# # 2. Encapsulation

# """
# All Object we create are encapsulation
# """

# # 3. Inheritance

# class Car:
#   @staticmethod
#   def start():
#     print("Car started!")
    
#   @staticmethod
#   def stop():
#     print("Car stop!")  

# class ToyottaCar(Car):
#   def __init__(self, name) -> None:
#     self.name = name

# c1 = ToyottaCar("cultus")
# print(c1.stop())


# 4. Polymorphism: Operator overloading

class Complex:
  def __init__(self, real , img) -> None:
    self.real = real
    self.img = img

  def showNumber(self):
    print(self.real,"i +", self.img, "j")

  def __add__(self,num2):
    newReal  = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal,newImg)
  
  def __sub__(self,num2):
    newReal  = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal,newImg)

c1 =  Complex(1,3)
c1.showNumber()

c2 =  Complex(3,5)
c2.showNumber()



c3 = c1 - c2
c3.showNumber()
