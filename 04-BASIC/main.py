# Python Encapsulation
# Encapsulation is about protecting data inside a class.

# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

# This prevents accidental changes to your data and hides the internal details of how your class works.


# Private Properties
# In Python, you can make properties private by using a double underscore __ prefix:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Here age is a private property

    # Here we access the private property

    # option1
    def info(self):
        return f"Hi my name is {self.name} and i am {self.__age} years old"

    # option2

    def get_age(self):
        return self.__age


p1 = Person("Jon", 25)

print(p1.info())

print(p1.get_age())
