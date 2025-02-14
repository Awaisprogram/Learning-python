#1.

 a = int(input("Enter first number: "))
 b = int(input("Enter second number: "))
 c = int(input("Enter third number: "))
 d = int(input("Enter fourth number: "))

 if a>=b and a>=c and a>=d:
   greatest = a
 elif b>=a and b>=c and b>=d:
   greatest = b

 elif c>=a and c>=b and c>=d:
   greatest = b
 else:
   greatest = d

 print(f"\nThe greatest number is: {greatest}")

#2.



English = int(input("Enter first number: "))
Urdu = int(input("Enter second number: "))
Maths = int(input("Enter third number: "))

a = English+Urdu+Maths
b = a*100
c = b/300
p = 40.0


if c>=p:
  print(f"Student is passed cuz total marks is {a} and percentage is {c}%")
elif English and Urdu and Maths == 33.0:
  print(f"Student is passed cuz marks of every subject is more than 30% and the total marks are {a} and percentage is {c}%")
else:
  print(f"You are Failed cuz marks are {a} and percentage is {c}%")
