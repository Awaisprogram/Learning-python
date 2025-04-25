# print("Hello World")

# for i in range(2,6,50):
#        print( i)

#        print("\n")


# for b in range(10,100,50):
#        print(b)

#        print("\ooo")

# for c in range(30,100,20):
#  print(c)   


# print("\t")       
       
# str="Shruti"
# print("string is ",str)

# var1 = str(input("My age is : " ))
# print(var1)

# print('hello world')





# STRING SLICING (chap-3)

# name = "Awais"
# sl = name[0:3] #Slice the  last 2 values
# print(sl)
#skip value
# var = "Amazing"
# sl = var[1:6:2] #Slice  till 6 after 2 values
# print(sl) 


# STRING FUNCTIONS

# 1.len function (returns length of string)


var = len("Awais")
print(var)

# 2.string.endswith() function (tells weather the function ends with the given value or not is boolean format (T/F))


var = ("Awais").endswith("ais")
print(var)

# 3.string.count("s") function (s counts the number of times ___ appears)


var = ("Awais").count("s")
print(var)  
#  s appear 1 time in Awais

# 4.string.capatalize() function (Capatalize the first latter)

var = ("awais").capitalize()
print(var)

# 5. string.find() function (used to find the first occurrence of a substring in a string)

var = ("Hello World").find("World")
print(var) 
#  'world' starts at index 7.
