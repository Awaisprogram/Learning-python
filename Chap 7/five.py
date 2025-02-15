# Chap 07 Loops in python

#Quick Quiz 1

#       WHILE LOOP

# 1.

i = 0
while i <= 50:
  print(f"\n{i}")
  i += 1

# 2.

i = 0
while i <= 20:
  print(i)
  if i == 10:
    break 
  i += 1

#Quick Quiz 2

content = ["Awais", "Waleed" , "Ali"]
i = 0
while i < len(content):
  print(content[i])
  i += 1

#       FOR LOOP

# 1.

content = ["Awais", "Waleed" , "Ali" ]  

for name in content:
     print(name)

#The break Statement

for i in range(40,80):
    print(i)    
    if i == 60:
        break 
    
#The continue Statement

for i in range(4):
    print("Printing")
    if i == 2:
        continue
    print(i)

#The Pass Statement   

content = ["Awais", "Waleed" , "Ali" ]  

for name in content:
     pass