#CHAP 4 List and tuples

# 1.

 fruits = []

 for i in range(7):
   fruit= input(f"Enter fruits {i+1} : ").capitalize()
   fruits.append(fruit)
   print("\nFruits you entered:", fruits)  

 guests = []

 for i in range(3):
   guest = input(f"Enter fruits {i+1} : ").capitalize()
   guests.append(guest)
   print(f"\n Guests you invited are: {guests}")

 dishes = []
 for i in range(3):
   dish = input(f"Enter dishes {i+1} : ")
   dishes.append(dish).capitalize()
   print(f"\n Dishes you insert are: {dishes}")

#2.

 marks = []
 for i in range(6):
   mark = input(f"Enter your marks {i+1} : ")
   marks.append(mark)
   marks.sort()
   print(f"\n Sorted! marks you insert are: {marks}")

#3.

 my_tuple = (1, 2, 3, 4, 5)
 my_tuple[0] = 10 
#return  TypeError: 'tuple' object does not support item assignment

 my_tuple = (10, 20, 30) 
 print(my_tuple)

# #4.

 numbers = [10, 20, 30, 40]  
 total = sum(numbers)
 print("The sum of the list is:", total)

 numbers = []
 for i in range(4):
   number = int(input(f"Enter number {i+1} : "))
   numbers.append(number)
   total = sum(numbers)
   print("\n The sum of the list is:", total)

#5.

 a = (7,0,8,0,0,9).count(0)
 print(a) 


############################################################################################
