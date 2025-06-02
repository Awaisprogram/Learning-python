# ##### Del keywords

# class Student:
#   def __init__(self, name) -> None:
#     self.name = name

# s1 = Student("Awais") 
# print(s1.name)   
# del s1
# print(s1.name)

###### Private (like) attributes and methods

# eg.1
# class Account:
#   def __init__(self, acc_no , acc_pass) -> None:
#     self.__acc_no = acc_no
#     self.acc_pass = acc_pass

# acc1 = Account("1234" , "abcd")    

# print(acc1.acc_no)

# eg.2

# class Person:
#   __name = "Person"

#   def __hello(self):
#     print("hello user!")

#   def welcome(self):
#     print(self.__hello())

# p1 = Person()
# # print(p1.__name)
# p1.welcome()



# <!-- Super Method -->

# class Car:
#   def __init__(self,type):
#     self.type = type

#   @staticmethod
#   def start():
#     print("Car started..")

#   @staticmethod
#   def stop():
#     print("Car Stopped..")

# class ToyotaCar(Car):
#   def __init__(self, name,type):
#     super().__init__(type)
#     self.name = name
#     super().start()
    

# car1 = ToyotaCar("Prius", "electric")
# print(car1.type)

# <!-- Class Method -->

# class Person:
#   name = "Awais"

#   # def changeName(self ,name):
#   #   self.__class__.name = name

#   @classmethod
#   def changeName(cls, name):
#     cls.name = name
     

# p1 = Person()
# p1.changeName("Awais shaikh")
# print(p1.name)
# print(Person.name)

# <!-- Property decorator -->

class Student:
  def __init__(self, phy , chem , maths) -> None:
    self.phy = phy
    self.chem = chem
    self.maths = maths
    

  # def calPercentage(self):
  #   self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
  @property
  def percentage(self):
    return  str((self.phy + self.chem + self.maths)/3) + "%"  
stu = Student(98,97,99)
print(stu.percentage)

stu.phy = 86
print(stu.phy)
stu.percentage
print(stu.percentage)
