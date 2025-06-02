# class Student:
#   def __init__(self, name,marks) :
#     self.name = name
#     self.marks = marks
    
#   def print_average(self):
#       sum = 0
#       for val in self.marks:
#          sum += val
#       print(f"Hi {self.name} Your average score is {sum/3}")   
         

# s1 = Student("Awais", [97, 80, 84])
# s1.print_average()



# class Account:
#   def __init__(self, bal, acc):
#     self.balance = bal
#     self.account_no = acc
#     user = int(input("Enter the account number : "))
#     if user == self.account_no:
#       print(f"\nBalance : {self.balance}\n")
#     else:
#       print("Invalid number") 

#   def debit(self, amount):
#        self.balance -= amount
#        print("Rs.", amount , "was debited")
#        print("Total balance =", self.get_balance())

#   def credit(self, amount):
#        self.balance += amount
#        print("Rs.", amount , "was credited")
#        print("Total balance =", self.get_balance())


#   def get_balance(self):
#      return self.balance     


    
# a1 = Account(10000, 12345)
# a1.debit(1000)
# a1.credit(500)


