import os

directory_path ='/'

# List all files and directories in the current directory
contents = os.listdir(directory_path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)

