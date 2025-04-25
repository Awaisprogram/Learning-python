#CHAP 4 List and tuples

# 1. Lists

frinds =["Awais", "Waleed", "Ratan lal", "Atma ram", "Bilal" , "Ahmed"]
print(frinds)

#Lists Indexing (like string and as I learned in ts)

L1 = [7,9,"Awais"]
L2 = L1[0:2]
print(L2) 

#List methods

# 1. List.sort()

List = [2,5,8,12,3,6]
List.sort()
print(List)

# 2. List.reverse()

List = [2,5,8,12,3,6]
List.reverse()
print(List)

# 3. List.append() (Add something at the end)

List = [2,5,8,12,3,6]
List.append(9)
print(List)

# 4. List.insert() (insert something at the given index)=> (index, no.)

List = [2,5,8,12,3,6]
List.insert(3,2)
print(List)


# 5. List.pop() (to delete)

List = [2,5,8,12,3,6]
List.pop(3)
print(List)

# 6. List.remove() (remove the mentioned no. from list)


List = [2,5,8,12,3,6]
List.remove(12)
print(List)

# Tuples

# 1. a.count()

a = (1,4,3,1).count(1)
print(a) #return 2 because a occurs twice 

# 2. a.index()

a = (1,4,3,1).index(4)
print(a) #return 1 because 4 occurs at index 1 
