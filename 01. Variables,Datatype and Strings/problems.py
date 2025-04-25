#Chap 1 Problem

import os

directory_path ='/'

# List all files and directories in the current directory
contents = os.listdir(directory_path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)

######################################

print('''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle little star
How I wonder what you are
When the blazing sun is gone
When he nothing shines upon
Then you show your little light
Twinkle, twinkle, all the night
Twinkle, twinkle, little star
How I wonder what you are
''')


######################################

#Chap-2 Problem

#SIMPLE CALCULATOR USING PYTHON (chap-2)

var2 = int(input("Enter first no. : " ))
var3 = int(input("Enter second no. : " ))
var=(var2)*(var3)
print(var)

#Chap-3 Problem

var1 = input("Enter your name: ")  
var2 = "Good Afternoon"
print(f"{var1}  {var2}")


#2

var1 = input("Enter your name: ") 
var3 = input("Enter Date: ")  
var2 = "Dear"
print(f"{var2} {var1},\n")  
print("You are selected!\n")
print(f"Date: {var3}")


