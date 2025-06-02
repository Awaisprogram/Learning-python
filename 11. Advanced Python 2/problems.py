from functools import reduce
# 1

# name = input("Enter name: ")
# marks = int(input("Enter marks: "))
# number = int(input("Enter phone number: "))

# s = "The name of student is {} his marks are {} adnd his phone number is {}".format(name, marks , number)

# print(s)

# 2

table = [str(7*i) for i in range(1,11)]
s="\n".join(table)
print(s)

# 3

def div(n):
  if(n%5 == 0):
    return True
  return False
a = [1 ,333 , 55 ,335, 2356 ]

f = list(filter(div, a))

print(f)

# 4

l = [1 ,333 , 55 ,335, 2356 ]

def greater(a,b):
  if(a > b):
    return a 
  return b
print(reduce(greater, l))

# 5




