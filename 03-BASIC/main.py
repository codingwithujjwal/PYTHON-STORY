#  All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

# basic class


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)


# Default Values in __init__()


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age


# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)


# Multiple Parameters


# class Person:
#     def __init__(
#         self,
#         name,
#         age,
#         city,
#         country,
#     ):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country


# p1 = Person("Linus", 30, "Oslo", "Norway")
# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello my name is {self.name} and i am {self.age} years old")


# p1 = Person("Emil", 25)

# p1.greet()
