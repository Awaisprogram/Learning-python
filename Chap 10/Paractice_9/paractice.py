# 1

with open("poem.txt") as f:
  print(f.read())

# 2 Game


# 3 Tables Generation

# 4

word = "Donkey"
with open("file.txt") as f:
  content = f.read()
  NewContent = content.replace(word,"######")
  with open("file.txt", "w") as f:
    f.write(NewContent)

# 5

words = ["Donkey", "Gandy", "Bad"]
with open("file.txt") as f:
  content = f.read()
  for word in words:
   content = content.replace(word, "#" * len(word))

  with open("file.txt", "w") as f:
    f.write(content)
    