# Chap 9 File I/O

#1. Read

f = open("file.txt")
data = f.read()
print(data)
f.close()

#2. write

st = "Hey Awais you are doing great"

f = open("myfile.txt", "w")

f.write(st)

f.close()


#3. Read lines

f = open("file.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()


#4. Read single line


f = open("file.txt")
line1 = f.readline()
print(line1,type(line1))
line2 = f.readline()
print(line2,type(line2))
line3 = f.readline()
print(line3,type(line3))
f.close()

# 4.(2)

f = open("file.txt")
line = f.readline()
while(line != ""):
  print(line)
  line = f.readline()
f.close()

# 5. Append

st = "Hey Awais you are doing great"

f = open("myfile.txt", "a")

f.write(st)

f.close()


# 6. With Statement

with open("file.txt") as f:
  print(f.read())

#Dont need to close file 
