name = input("Enter your name: ")
marks = {
    "Awais": "70",
    "Waleed": "50",
    "Ali": "60",
}


if name in marks:
    print(f"Your result is in the list. You scored {marks[name]} marks.")
else:
    print("Your result is not in the list.")

 #2   

first = int(input("Enter your numbers: "))

second = int(input("Enter your numbers: "))

if first >= second:
    print("Your Marks is greater")
else:
    print("Your Marks is not greater")
#3

username = input("Enter comment: ")
names = ["Awais","Waleed","Misbah", "Ali"]
if any(name.lower() in username.lower() for name in names):
    print("Your name is in the list")   
else:
     print("Your name is not in the list")       