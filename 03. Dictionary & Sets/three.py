#CHAP 5 DICTIONARY AND SETS
#DICTIONARY
 
a ={
  "key" : "value",
  "name" : "Awais",
}
print(f"DICTIONARY : \n{a}")

#DICTIONARY METHODS

#1. dictionary.items() return a list of (key,value) tuples

a ={
  "key" : "value",
  "name" : "Awais",
}.items()
print(f"\ndictionary.items: {a}")

#2. dictionary.keys() return a list of keys 

a ={
  "key" : "value",
  "name" : "Awais",
}.keys()
print(f"\ndictionary.keys: {a}")

#3. dictionary.update() update the dictionary with supplied key-value pairs

a = {
  "keys" : "something",
  "marks" : "100",
}
a.update({"name": "Awais"})

print(f"\ndictionary.update : {a}")

#4. dictionary.get() returns the value of specified keys

a = {
  "name": "Awais",
  "class": "Inter",
  "Course" :"CS"
}.get("Course")
print(f"\ndictionary.get : {a}")

#SETS

sets = {1,2,3}
sets.discard(2)
print(sets)
