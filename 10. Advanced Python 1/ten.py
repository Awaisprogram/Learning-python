# Advance Python

from typing import List, Union ,Tuple
from module import myFunc

# Walrus operator

# if(n:= len([1,2,3,4,5])) > 3:
#   print(f"The list is too long ({n} elements, expected ,<=3)")

# # Type Definations

# n : int = 5

# name : str = "Awais"

# def sum(a:int,b:int)-> int:
#   return a + b

# sum(2,3)

# Match

# def http_status(status): 
#     match status:  
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"  


# print(http_status(200))

# Dictionar merge

# dic1 ={
#     "a" : 1,
#     "b" : 2
# }

# dic2 ={
#     "b" : 3,
#     "c" : 4
# }

# merged = dic1 | dic2

# print(merged)

# Exception handling

# try:
#     a = int(input("Hey Enter a number: "))
#     print(a)   
# except Exception as e:
#     print(e)

# print("Thanks")

# Specific Error
   
# try:
#     a = int(input("Hey Enter a number: "))
#     print(a)  

# except ValueError as v:
#     print("Heyyy")
#     print(v)     

# except Exception as e:
#     print(e)

# print("Thanks")  

# Raising Exception

# a = int(input("Enter a number : "))
# b = int(input("Enter a number :"))
# if(b==0):
#     raise ZeroDivisionError("You can not Divide with Zero")
# else:
#     print(f"The divison of a/b is {a/b}")

# Try with else    

# try:
#     a = int(input("Hey Enter a number: "))
#     print(a)  


# except Exception as e:
#     print(e)

# else:
#     print("I am inside else")

# Try with Finally    

# def main():
#   try:
#       a = int(input("Hey Enter a number: "))
#       print(a)  


#   except Exception as e:
#       print(e)

#   finally:
#       print("I am inside finally")

# main()

# Global Keyword

a = 89
def fun():
  global a
  a = 3
  print(a)


fun()  
print(a)

# Enamurate

l = [1,23,36,43]

# index = 0
# for item in l:
#   print(f"The item number {index} is {item}")
#   index +=1

# This is can be simplify using enamurating function

for index,item in enumerate(l):
   print(f"The item number {index} is {item}")


# List Comprehension  

l = [1,2,3,4]

# sqauredList = []

# for item in l:
#    sqauredList.append(item*item)
# print(sqauredList)  

sqauredList = [i*i for i in l]
print(sqauredList)

