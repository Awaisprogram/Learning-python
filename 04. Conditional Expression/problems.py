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

# 3

comment = input("Enter comment: ")
spam = ["make a lot money","buy now","subscribe this", "click this"]
print(spam)
if any(keyword in comment.lower() for keyword in spam):
   print(f"Spam detected: {comment}")
else:
  print(f"No Spam detected: {comment}") 

#4.

username =input('Enter username: ')
number = len(username)
print(f"\nUsername length: {number}")
if number>=10:
   print(f"\nGreater or equal to 10")
else:
    print(f"\less than 10")

# 5.

username = input("Enter comment: ")
names = ["Awais","Waleed","Misbah", "Ali"]
print(names)
if any(name.lower() in username.lower() for name in names):
   print(f"Name is in the list: {username}")
else:
  print(f"Name is not in the list: {username}") 

# 6.

marks = int(input("Enter Marks: "))

if 90 <= marks <= 100:
    print("Ex")
elif 80 <= marks <= 89:
    print("A")
elif 70 <= marks <= 79:
    print("B")
elif 60 <= marks <= 69:
    print("C")
elif 50 <= marks <= 59:
    print("D")
else:
    print("F")


#7.

post = input("Enter comment: ")
talks = ["Awais"]
print(talks)
if any(talk.lower() in post.lower() for talk in talks):
   print(f"Name is in the list: {post}")
else:
  print(f"Name is not in the list: {post}") 
