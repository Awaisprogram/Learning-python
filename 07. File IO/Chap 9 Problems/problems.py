# 1

f = open("poem.txt")
content = f.read()
if("Twinkle" in content):
  print("Twinkle is present in content")
else:
  print("Twinkle is not present in content")  
f.close()

# With Mthod

with open("poem.txt" ) as f:
  print(f.read())

# 4  

word = "Donkey"

with open("file.txt") as f:
  content = f.read()

NewContent = content.replace(word, "######")

with open("file.txt", "w") as f:
  content = f.write(NewContent)

# 5

words = ["Donkey", "Bad", "Ganda"]

with open("file.txt") as f:
  content = f.read()
for word in words: 
  content = content.replace(word, "#" * len(word))


with open("file.txt", "w") as f:
  content = f.write(content)

# 6

with open("log.txt") as f:
  content = f.read()
if("python" in content):
  print("Yes python is present")
else:
  print("python is not present")  
  
# 7

with open("log.txt") as f:
  lines = f.readlines()

lineno = 1
for line in lines:  
 if("python" in line):
      print(f"Yes python is present in line no. {lineno}")
      break
 lineno +=1
else:
  print("python is not present")

# 8

with open("this.txt") as f:
  content = f.read()

with open("this_copy.txt", "w") as f:
  f.write(content)

# 9 

with open("this.txt") as f:
  content = f.read()

with open("this_copy.txt") as f:
  content1 = f.read()

if (content == content1):
  print("Yes these files are identical")
else:
  print("No these files are identical")


# 10 to blank

with open("this_copy.txt", "w") as f:
  f.write(" ")

#  11

with open("old.txt") as f:
  content1 = f.read()

with open("rename_by_python.txt", "w") as f:
  f.write(content1)

