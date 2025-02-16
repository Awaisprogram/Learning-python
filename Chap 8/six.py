# Chap 8 Functions and Recursions

# def func1():
#   print("Hello")

# func1()  

# Quick Quiz 1

# def greeting(name):
#   print(f"Hello {name}")
# greeting("Awais")  
# greeting("Waleed")

# Fuction with arguments

# def goodDay(name):
#   print(f"Good Day {name}")

# goodDay("Awais")

# Return functions:

# 1

# def return_f(a,b):
#   sum = a + b
#   return sum
# print(return_f(10,5))
# print(return_f(15,5))

# 2

# def greater():
#   a = int(input("Enter the number: "))
#   b = int(input("Enter the number: "))
#   if a > b:
#     return a
#   else: 
#     return b
# result = greater()
# print(f"{result} is greater")  

# Default Argument

# def goodDay(name="Waleed"):
#   print(f"Good Day {name}")

# goodDay("Awais")



#  Recursions

# Factorial 1 and 0 = 1

def factorial(n):
  if(n == 1 or n == 0):
    return 1
  return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of {n}  is {factorial(n)}")