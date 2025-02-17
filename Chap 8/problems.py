# 1

n = int(input("Enter a number: "))
for i in range(1,11):
  print(f"{n} x {i} = {n*i}")

# 2

l = ["Awais", "Waleed", "Ali", "Zahir"]
for name in l:
  if (name.startswith("A")):
    print(f"Greet {name}")

# 3

n = int(input("Enter a number: "))
i = 1
while (i < 11): 
  print(f"{n} x {i} = {n*i}")
  i += 1

#4

n = int(input("Enter a number: "))

for i in range(2,n):
  if(n%i) == 0:
    print("Not a prime number")
    break
  else:
    print("A prime number")
  

 #5

n = int(input("Enter a number: "))
i = 1
sum = 0
while(i<=n):
  sum += i
  i +=1
print(sum)

#6

n = int(input("Enter a number: "))
product = 1 

for i in range(1, n + 1):
    product *= i 

print(f"The factorial of {n} is {product}")

#7

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"* (2*i-1),end="")
    print("")

#8

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*"* i,end="")
    print("")

#9

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if(i == 1 or i == n):
       print("*" * n)
    else:
         print("*", end="")
         print(" " * (n - 2), end="")
         print("*")

#10

n = int(input("Enter a number: "))
for i in range(1, 11):
  print(f"{n} x {11-i} = {n*(11-i)}")