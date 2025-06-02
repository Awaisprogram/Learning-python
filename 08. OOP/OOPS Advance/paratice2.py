class Car:
  def __init__(self, brand):
    self.brand = brand

  def car_brand(self):
    self.brand = "Toyota"  
    
    

c1 = Car("Mehran")
print(c1.brand)




class Circle:
  def __init__(self, radius) -> None:
    self.radius = radius

  def area(self):
    return (22/7) * self.radius ** 2  
  
  def parameter(self):
    return 2 * (22/7) * self.radius
  
c1 = Circle(21)
print(c1.area())
print(c1.parameter())

# 


class Employee:
  def __init__(self,role , dept , salary) -> None:
    self.role = role
    self.dept = dept
    self.salary = salary

  def showDetails(self):
    print(f"role = {self.role}")  
    print(f"dept = {self.dept}")  
    print(f"salary = {self.salary}")

class Engineer(Employee):
      def __init__(self, name , age) -> None:
         self.name = name
         self.age = age
         super().__init__("Engineer" , "IT" , "750000")

      def showDetails(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        super().showDetails()   

e1 = Engineer("Elon Musk",  "40")
e1.showDetails()


# 

class Order:
  def __init__(self,item , price) -> None:
    self.item = item
    self.price = price

  def __gt__(self, o2):
    return self.price > o2.price  


o1 = Order("chips", 20)
o2 = Order("tea", 15)
print(o1>o2)