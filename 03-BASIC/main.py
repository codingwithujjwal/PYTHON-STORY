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


# Class Properties and Access Properties


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


# car1 = Car("Toyota", "Corolla")

# print(car1.model)
# print(car1.brand)


# Modify Properties


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Hi my name is {self.name} and i am {self.age} years old.."


# p1 = Person("Tobias", 25)

# print(p1.info())

# p1.age = 26

# print(p1.info())


# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def __str__(self):
#         return f"Hi my name is {self.name} and i am {self.age} years old.."


# p1 = Person("Tobias", 25, "Rusia")

# print(p1)


# Python Inheritance


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f"Hi my first name is {self.fname} and last name is {self.lname}")


x = Person("John", "Doe")

x.printName()


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2020

    def Welcome(self):
        print(
            f"Welcome {self.fname} {self.lname}, to the class of {self.graduationyear}"
        )


y = Student("Mike", "Olsen")
# y.printName()
# print(y.graduationyear)

# print(y.Welcome())
y.Welcome()
