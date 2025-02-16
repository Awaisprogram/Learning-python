#1

#Table using for loop

# n = int(input("Enter a number: "))
# for i in range(1,11):
#   print(f"{n} x {i} = {n * i}")

#2

#Table using While loop

# n = int(input("Enter a number: "))
# i = 0
# while i < 10:
#   i += 1
#   print(f"{n} x {i} = {n * i}")

#3

#Greetings

# l = ["Awais", "Waleed", "Ali", "Zahir"]
# for name in l:
#   if(name.startswith("A")):
#     print(f"Greetings {name}")

# 4 

# sum

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while(i<=n):
#   sum += i
#   i += 1
# print(sum)

# 4 

#   *
#  ***
# *****

# n = int(input("Enter a number: "))
# for i in range(1 , n+1):
#   print(" " * (n-i) ,end="")
#   print("*" * (2*i-1),end='')
#   print('')

# 5 

#  *
#  **
#  ***

n = int(input("Enter a number: "))
for i in range(1,n+1):
  print("*" * (i), end="")
  print('')
