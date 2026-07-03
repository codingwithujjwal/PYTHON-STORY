# age=int(input("Plese provide your age: "))

# if age<10:
#     print(f"your age is {age} so you are chield ")

# elif age < 18:
#     print(f"your age is {age} so you are boy")

# elif age >=18:
#     print(f"your age is {age} so you can vote")

# else:
#     print("Plese provide me your age ")

# ------------------------------function---------------------

# def my_function(name):
#     print(f"Hello {name} welcome to my site")

# my_function("ujjwal")


# animal_type=input("Enter your animal type: ")
# name=input("Enter your animal name: ")

# def animal_details(animal_type,name):
#     print(f"I have a {animal_type} and its name is {name}")

# animal_details(animal_type,name)

# def my_function(x,y):
#     return x+y

# result=my_function(5,5)
# print(result)

# def my_numbers(*num):
#     total=0
#     for i in num:
#         total += i

#     return total

# print(my_numbers(1,2,3))


# find maximum numbers

# 12,1,2,3,4,5,55,85

# def find_maxnum(*numbers):
#     if len(numbers) == 0 :
#         return None

#     max_num = numbers[0]

#     for i in numbers:
#         if i > max_num:
#             max_num = i

#     return max_num

# print(find_maxnum(12,1,2,3,4,5,55,85))

# def change_to_upper_case(func):
#     def inner():
#         return func().upper()

#     return inner

# @change_to_upper_case
# def my_function():
#     return "hello sir"

# print(my_function())


# def change_to_upper_case(fnc):
#     def inner(x):
#         return fnc(x).upper()
#     return inner

# @change_to_upper_case

# def my_function(name):
#     return f"hello my name is {name}"

# print(my_function("jon"))


# ------------------------------------Lambda Functions---------------------------------


# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.


# Syntax
# lambda arguments : expression

# x=lambda a: a+20

# print(x(5))


# x=lambda a,b : a*b
# print(x(5,6))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     else:
#         return n * factorial(n-1)

# print(factorial(5))


# -------------------------------------Python Iterators--------------------------------------

# An iterator is an object that contains a countable number of values.

# mytupple=("apple","banana","cherry")
# myit=iter(mytupple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myClass=myNumbers()
# myiter=iter(myClass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Stop after 20 iterations:

# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
    # def __iter__(self):
        # self.a = 1
        # return self

    
    # def __next__(self):
        # if self.a <= 20:
            # x = self.a
            # self.a += 1
            # return x
        # else:
            # raise StopIteration




# myClass = myNumbers()
# myiter = iter(myClass)


# for i in myiter:
    # print(i)


# -------------------------------------Python Datetime--------------------------------------

# import datetime

# x = datetime.datetime.now()

# print(x)
# age=int(input("Plese provide your age: "))

# if age<10:
#     print(f"your age is {age} so you are chield ")

# elif age < 18:
#     print(f"your age is {age} so you are boy")

# elif age >=18:
#     print(f"your age is {age} so you can vote")

# else:
#     print("Plese provide me your age ")

# ------------------------------function---------------------

# def my_function(name):
#     print(f"Hello {name} welcome to my site")

# my_function("ujjwal")


# animal_type=input("Enter your animal type: ")
# name=input("Enter your animal name: ")

# def animal_details(animal_type,name):
#     print(f"I have a {animal_type} and its name is {name}")

# animal_details(animal_type,name)

# def my_function(x,y):
#     return x+y

# result=my_function(5,5)
# print(result)

# def my_numbers(*num):
#     total=0
#     for i in num:
#         total += i

#     return total

# print(my_numbers(1,2,3))


# find maximum numbers

# 12,1,2,3,4,5,55,85

# def find_maxnum(*numbers):
#     if len(numbers) == 0 :
#         return None

#     max_num = numbers[0]

#     for i in numbers:
#         if i > max_num:
#             max_num = i

#     return max_num

# print(find_maxnum(12,1,2,3,4,5,55,85))

# def change_to_upper_case(func):
#     def inner():
#         return func().upper()

#     return inner

# @change_to_upper_case
# def my_function():
#     return "hello sir"

# print(my_function())


# def change_to_upper_case(fnc):
#     def inner(x):
#         return fnc(x).upper()
#     return inner

# @change_to_upper_case

# def my_function(name):
#     return f"hello my name is {name}"

# print(my_function("jon"))


# ------------------------------------Lambda Functions---------------------------------


# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.


# Syntax
# lambda arguments : expression

# x=lambda a: a+20

# print(x(5))


# x=lambda a,b : a*b
# print(x(5,6))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     else:
#         return n * factorial(n-1)

# print(factorial(5))


# -------------------------------------Python Iterators--------------------------------------

# An iterator is an object that contains a countable number of values.

# mytupple=("apple","banana","cherry")
# myit=iter(mytupple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myClass=myNumbers()
# myiter=iter(myClass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Stop after 20 iterations:

# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# myClass=myNumbers()
# myiter=iter(myClass)


# for i in myiter:
#     print(i)


# -------------------------------------Python Datetime--------------------------------------

# import datetime

# x = datetime.datetime.now()

# print(x)
# age=int(input("Plese provide your age: "))

# if age<10:
#     print(f"your age is {age} so you are chield ")

# elif age < 18:
#     print(f"your age is {age} so you are boy")

# elif age >=18:
#     print(f"your age is {age} so you can vote")

# else:
#     print("Plese provide me your age ")

# ------------------------------function---------------------

# def my_function(name):
#     print(f"Hello {name} welcome to my site")

# my_function("ujjwal")


# animal_type=input("Enter your animal type: ")
# name=input("Enter your animal name: ")

# def animal_details(animal_type,name):
#     print(f"I have a {animal_type} and its name is {name}")

# animal_details(animal_type,name)

# def my_function(x,y):
#     return x+y

# result=my_function(5,5)
# print(result)

# def my_numbers(*num):
#     total=0
#     for i in num:
#         total += i

#     return total

# print(my_numbers(1,2,3))


# find maximum numbers

# 12,1,2,3,4,5,55,85

# def find_maxnum(*numbers):
#     if len(numbers) == 0 :
#         return None

#     max_num = numbers[0]

#     for i in numbers:
#         if i > max_num:
#             max_num = i

#     return max_num

# print(find_maxnum(12,1,2,3,4,5,55,85))

# def change_to_upper_case(func):
#     def inner():
#         return func().upper()

#     return inner

# @change_to_upper_case
# def my_function():
#     return "hello sir"

# print(my_function())


# def change_to_upper_case(fnc):
#     def inner(x):
#         return fnc(x).upper()
#     return inner

# @change_to_upper_case

# def my_function(name):
#     return f"hello my name is {name}"

# print(my_function("jon"))


# ------------------------------------Lambda Functions---------------------------------


# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.


# Syntax
# lambda arguments : expression

# x=lambda a: a+20

# print(x(5))


# x=lambda a,b : a*b
# print(x(5,6))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     else:
#         return n * factorial(n-1)

# print(factorial(5))


# -------------------------------------Python Iterators--------------------------------------

# An iterator is an object that contains a countable number of values.

# mytupple=("apple","banana","cherry")
# myit=iter(mytupple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x

# myClass=myNumbers()
# myiter=iter(myClass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Stop after 20 iterations:

# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration


# myClass=myNumbers()
# myiter=iter(myClass)


# for i in myiter:
#     print(i)


# -------------------------------------Python Datetime--------------------------------------

# import datetime

# x = datetime.datetime.now()

# print(x)
