# how to print a statement

# print("Hello python")

# python variables
# a=20
# b="Hello"
# print(a)
# print(b)

# data types in python

# a=20

# Python Numbers
# There are three numeric types in Python:

# int
# float
# complex

# x=20
# y=11.3
# z=1j

# print(type(x))
# print(type(y))
# print(type(z))

# -----------------------STRING-----------------------

# str="hello world"
# print(str.capitalize())

# ----------------------LIST---------------

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))
# mylist.append("mango") 
# print(mylist)

# mylist.clear()
# print(mylist)

# mylist2=[]
# mylist2=mylist.copy()
# print(mylist2)

# print(mylist.count("apple"))

# fruits = ['apple', 'banana', 'cherry']

# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)
# print(fruits)

# fruits = ['apple', 'cherry', 'banana']

# print(fruits.index("cherry"))

# fruits.insert(1,"Mango")
# print(fruits)

# fruits.pop(1)
# print(fruits)

# fruits.remove("banana")
# print(fruits)

# fruits.reverse()
# print(fruits)

# fruits.sort()
# print(fruits)


# --------------------------Tupples--------------------------

# A tuple is a collection which is ordered and unchangeable.

# mytuple = ("apple", "banana", "cherry")

# print(mytuple[1])  # access a tupple

# for x in mytuple:
#     print(x)

# for i in range(len(mytuple)):
#     # print(i)
#     # print(mytuple[i])
#     print(f"This tupple index is {i} and value is {mytuple[i]}")

# i=0
# while i< len(mytuple):
#     print(f"This tupple index is {i} and value is {mytuple[i]}")
#     i+=1

# ----------------------PYTHON-SETS---------------------------------------

# thisSet = {"apple", "banana", "cherry"}


# for i in thisSet:
#     print(i)

# thisSet.add("orange")
# print(thisSet)

# To add items from another set into the current set, use the update() method.

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)
# print(thisset)


# To remove an item in a set, use the remove(), or the discard() method.

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# thisset.discard("banana")
# print(thisset)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

# thisset = {"apple", "banana", "cherry"}
# thisset.pop()
# print(thisset)

# The clear() method empties the set:

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()
# print(thisset)

# The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# You can loop through the set items by using a for loop:

# thisset = {"apple", "banana", "cherry"}

# for i in thisset:
#     print(i)



# The union() method returns a new set with all items from both sets.

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3=set1.union(set2)
# set3=set1 |set2
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# set5=set1.union(set2,set3,set4)
# set5=set1 | set2 | set3 | set4
# print(set5)

# The union() method allows you to join a set with other data types, like lists or tuples.

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z=x.union(y)
# print(z)


# The intersection() method will return a new set, that only contains the items that are present in both sets.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3=set1.intersection(set2)
# print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3=set1 & set2
# print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)
# print(set1)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3=set1.difference(set2)
# set4=set2.difference(set1)
# print(set3)
# print(set4)

# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)
# print(set1)

# mySet=frozenset({"apple", "banana", "cherry"})
# print(type(mySet))

# 	Returns a shallow copy

# mySet2=mySet.copy()
# print(mySet2)

# a = frozenset({1, 2, 3, 4})
# b = frozenset({3, 4, 5})

# print(a.difference(b))
# print(a-b)

# Returns a new frozenset with the intersection

# a = frozenset({1, 2, 3, 4})
# b = frozenset({3, 4, 5})
# print(a.intersection(b))
# print(a&b)

# 	Returns True if there is NO intersection between two frozensets

# a = frozenset({1, 2})
# b = frozenset({3, 4})
# c = frozenset({2, 3})

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# Returns True if this frozenset is a (proper) subset of another

# a = frozenset({1, 2})
# b = frozenset({1, 2, 3})

# print(a.issubset(b))
# print(a <=b)
# print(a <b)

# 	Returns a new frozenset containing the union

# a = frozenset({1, 2})
# b = frozenset({2, 3})

# print(a.union(b))
# print(a |b)

# ----------------------------- Dictionaries----------------------------------

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict["brand"])

# There is also a method called get() that will give you the same result:

# print(thisdict.get("model"))

# The keys() method will return a list of all the keys in the dictionary.

# print(thisdict.keys())
# print(thisdict)

# thisdict["color"]="Gray" # Add property
# print(thisdict)

# The values() method will return a list of all the values in the dictionary.

# print(thisdict.values())

# if "model" in thisdict:
#      print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Update the "year" of the car by using the update() method:

# thisdict.update({"year":2025})
# print(thisdict)

# myFamily={
#     "chield1":{
#         "name":"person1",
#         "email":"person1@gmail.com"
#     },
#     "chield2":{
#         "name":"person2",
#         "email":"person2@gmail.com"
#     },
#     "chield3":{
#         "name":"person3",
#         "email":"person3@gmail.com"
#     }
# }

# # print(myFamily["chield3"]["name"])

# for x,obj in myFamily.items():
#     print(x)

#     for y in obj:
#         print(f"{y} : {obj[y]}")