# 1

def fun(name):
  print(f"Have a nice day {name}")
fun("Awais")  

#2

def fun2():
  a = int( input("Enter a number:"))
  b = int( input("Enter a number:"))
  result =  a+b

  print(result)  
fun2()

#3

def fun3(n):
    if n == 1:
        return 1 
    return fun3(n - 1) + n
print(fun3(4))


       
 
