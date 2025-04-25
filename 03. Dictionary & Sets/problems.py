#1.

words = {
  "dost" : "friend",
  "bhai" : "brother",
  "bhen" : "sister",
  }
word = input("Enter the word to get meaning : ")
print(words[word])

#2.

s = set()
for i in range(8):
  a= input(f"Enter number {i+1} : ")
  s.add(int(a))
  print(s)

#3.

d = {}  

for i in range(4):
    name = input(f"Enter friend's name {i+1}: ").capitalize()  
    lang = input(f"Enter Language for {name}: ").capitalize()  
    d.update({name:lang})

print(f"\nHere is the result: {d}")  # Print 

 
