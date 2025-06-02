# venv Virtual enviroment
from functools import reduce

"""
To install different version of module in env

"""

# pip freeze

# pip3 freeze > requirements.txt
"""

this commad will create a file where every packages whould be shown

"""
# pip3 install -r requirements.txt


"""

this commad will download packages in given file

"""

# Lambda function

def square(n):
  return n*n
print(square(3))

# Lambda function

# Examples:

square = lambda x : x * x
print(square(3))

sum = lambda a,b,c: a + b+ c
print(sum(3,2,5))

# Join Method

a = ["Awais", "Waleed" , "Ali"]
final = "::".join(a)
print(final)

# Format Method

a = "{0} is a good {1}".format("Awais", "Boy")
print(a)

# Map Example

l = [1,2,3,4,5]

square = lambda x : x * x
sqList = map(square, l)
print(list(sqList))

# Filter Example

def even(n):
  if (n%2 == 0):
    return True
onlyEven = filter(even,l)  
print(list(onlyEven)) 

# Reduce Example

def sum(a,b):
  return a + b
print(reduce(sum,l))
  


