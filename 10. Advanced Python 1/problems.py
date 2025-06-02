#1
try:
  with open("1.txt") as f:
    print(f.read())
except Exception as e:
  print(e)
try:
  with open("2.txt") as f:
    print(f.read())
except Exception as e:
  print(e)    
try:  
  with open("3.txt") as f:
    print(f.read())
except Exception as e:
  print(e)  

# 2  

# l = [1,2,3,4,5,6,7,8]

# for i, item in enumerate(l):
#   if i == 2 or i == 4 or i == 6:
#     print(item)

# 3


# n = int(input("Hey Enter a number: "))

# table = [n * i for i in range(1,11)]
# print(table)


# 4

# a = int(input("Enter a number : "))
# b = int(input("Enter a number :"))
# if(b==0):
#     raise ZeroDivisionError("You can not Divide with Zero")
# else:
#     print(f"The divison of a/b is {a/b}")

# 5


n = int(input("Hey Enter a number: "))

table = [n * i for i in range(1,11)]
with open(f"table.txt" , "a") as f:
  f.write(f"The table of {n}: {str(table)}\n")