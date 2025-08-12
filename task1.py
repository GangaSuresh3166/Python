# Task 1:

# Take user input for grocery items and pantry items
# grocery = input("Enter grocery items (comma-separated): ").split(",")
# pantry = input("Enter pantry items you already have (comma-separated): ").split(",")

# final=[]
# for item in grocery:
#     if item not in pantry:
#         final.append(item)
# print("\n Final list of items to buy:")
# for item in final:
#     print("-",item)


# Task 3:

# name=input("What's your name?")
# age=int(input("How old are you?"))
# print(f"Hello,{name}! You are {age} year old.")


# Task 4:

# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# if (num1>num2):
#     num1=num1+10
# else:
#     num1=num1-5
# print("Updated first number:",num1)

# Task 5:

# name=input("Enter your name:")
# age=input("Enter your age:")
# favorite_number=int(input("Enter your favorite number:"))
# print(f"Hello,{name}! You are {age} years old, and your favorite number is {favorite_number}.")


# task 12:

# def calculate_total(p,t=5):
#        return p+(p*t/100)
# print(calculate_total(100))


# items=[]
# def add_item(item):
#       global items
#       items.append(item)
# add_item("apple")
# print(items)


# task 13:

# def reverse_string(s):
#        if len(s)==0:
#               return s
#        else:
#               return reverse_string(s[1:])+s[0]
# print(reverse_string("hello"))


# square=lambda x:x*x
# print(square(7))


# task 15:

# favourite_foods=["pizza","burger","pasta","icecream","biriyani"]
# for food in favourite_foods:  
#       print(f"I love eating {food}.")


# task 16:

# square=[x**2 for x in range(1,11)]
# print(square)

# text="python programming is fun!"
# vowels=[ch for ch in text if ch.lower() in "aeiou"]
# print(vowels)

# numbers=list(range(1,21))
# odd_numbers=[n for n in numbers if n % 2 !=0]
# print(odd_numbers)


# task 17:

# text="programming"
# print(text[0],text[-1])
# reversed_text=text[::-1]
# print(reversed_text)
# print(text.count("m"))
# sentence="python is fun to learn"
# print(sentence.replace(" ","_"))
# word="madam"
# print(word==word[::-1])

# task 18:

# students=["Alice","Bob","Charlie"]
# grades=[85,90,78]
# student_grades=dict(zip(students,grades))
# print(student_grades)

# list1=[1,2,3]
# list2=[4,5,6]
# sum_list=[a+b for a,b in zip(list1,list2)]
# print(sum_list)

# zipped=zip(list1,list2)
# list_a,list_b=zip(*zipped)
# print(list_a)
# print(list_b)

# task 19:

# days=("monday","tuesday","wednedsay","thursday","friday","saturday","sunday")
# print(days[0])
# print(days[-1])
# print(days[2:5])
# print(days.index("wednesday"))

# student_list=["alice","bob","charlie","alice","david","bob"]
# unique_students=set(student_list)
# print(unique_students)
# set1={1,2,3,4}
# set2={3,4,5,6}
# print(set1|set2)
# print(set1&set2)
# print(set1-set2)
# print({1,2}.issubset(set1))

# task 20:

# import copy
# nested_list=[[1,2,3],[4,5,6]]
# shallow_copy=copy.copy(nested_list)
# nested_list[0][0]=99
# print("original list:",nested_list)
# print("shallow:",shallow_copy)

# while True:
#        try:
#              num=int(input("Enter a number:"))
#              print(f"you entered:{num}")
#              break
#        except ValueError:
#              print("invalid input! please enter a valid integer.")

# task 21

# import copy
# nested_list = [[1, 2, 3], [4, 5, 6]]
# shallow_copy = copy.copy(nested_list)
# nested_list[0][0] = 99
# print("Original list:", nested_list)
# print("Shallow copy :", shallow_copy)


# while True:
#     try:
#         num = int(input("Enter a number: "))
#         print(f"You entered: {num}")
#         break
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")


# task 22:

# class Book:
#     def _init_(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def apply_discount(self, discount_percent):
#         self.price -= self.price * (discount_percent / 100)
#     def describe(self):
#         print(f"Book: {self.title} by {self.author}, Price: ₹{self.price:.2f}")
# class SpecialEditionBook(Book):
#     def _init_(self, title, author, price, special_feature):
#         super()._init_(title, author, price)
#         self.special_feature = special_feature
#     def describe(self):
#         print(f"Special Edition: {self.title} by {self.author}, Price: ₹{self.price:.2f}, Feature: {self.special_feature}")
# book1 = Book("Python Basics", "John Smith", 500)
# book1.apply_discount(10)
# book1.describe()
# special_book = SpecialEditionBook("Advanced Python", "Jane Doe", 1000, "Autographed Copy")
# special_book.apply_discount(15)
# special_book.describe()


# task 23:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Employee(Person):
#     def __init__(self, name, age, employee_id):
#         super().__init__(name, age)
#         self.employee_id = employee_id
# person = Person("Alice", 30)
# employee = Employee("Bob", 40, "E12345")
# print(f"Person: {person.name}, Age: {person.age}")
# print(f"Employee: {employee.name}, Age: {employee.age}, ID: {employee.employee_id}")

# task 24:

# class BankAccount:
#     def __init__(self, account_number, balance=0.0):
#         self.__account_number = account_number 
#         self.__balance = balance  
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, new_balance):
#         if new_balance >= 0:
#             self.__balance = new_balance
#         else:
#             print("Balance cannot be negative!")

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive!")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Invalid withdrawal amount!")
# acc = BankAccount("12345", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# print("Balance:", acc.get_balance())



# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car engine started.")

#     def stop(self):
#         print("Car engine stopped.")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike started.")

#     def stop(self):
#         print("Bike stopped.")
# vehicles = [Car(), Bike()]
# for v in vehicles:
#     v.start()
#     v.stop()



# class Shape:
#     def area(self):
#         return 0

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.1416 * (self.radius ** 2)

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2
# shapes = [Circle(5), Square(4)]
# for s in shapes:
#     print(f"{s.__class__.__name__} area:", s.area())



# task 25:

# class Matrix:
#     def __init__(self, data):
#         self.data = data
#         self.rows = len(data)
#         self.cols = len(data[0])

#     def __mul__(self, other):
#         if self.cols != other.rows:
#             raise ValueError("Matrix dimensions do not match for multiplication.")
        
#         result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 for k in range(self.cols):
#                     result[i][j] += self.data[i][k] * other.data[k][j]
        
#         return Matrix(result)

#     def __str__(self):
#         return "\n".join(str(row) for row in self.data)


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     def __gt__(self, other):
#         return self.pages > other.pages
# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[5, 6], [7, 8]])
# m3 = m1 * m2
# print("Matrix Multiplication Result:")
# print(m3)
# book1 = Book("Python Basics", 250)
# book2 = Book("Advanced Python", 300)
# print("\nIs book2 bigger than book1?", book2 > book1)




# class Book:
#     count = 0

#     def __init__(self, title):
#         self.title = title
#         Book.count += 1
#     def total_books(cls):
#         return f"Total books created: {cls.count}"
# book1 = Book("Python Basics")
# book2 = Book("Advanced Python")
# print(Book.total_books())




# task 27:

# file_path = "example.txt"
# line_count = 0
# with open(file_path, "r") as file:
#     for line in file:
#         print(line.strip())  
#         line_count += 1
# print(f"Total number of lines: {line_count}")



# import datetime
# log_file = "activity_log.txt"
# with open(log_file, "w") as file:
#     file.write(f"User logged in at {datetime.datetime.now()}\n")
# with open(log_file, "a") as file:
#     file.write(f"User logged out at {datetime.datetime.now()}\n")
# with open(log_file, "r") as file:
#     print(file.read())




# source_file = "image.jpg"
# destination_file = "copy_image.jpg"
# with open(source_file, "rb") as src:
#     with open(destination_file, "wb") as dst:
#         dst.write(src.read())
# print("File copied successfully!")


# task 28:

# import pickle
# students = [
#     {"name": "Alice", "age": 20, "grade": "A"},
#     {"name": "Bob", "age": 22, "grade": "B"},
#     {"name": "Charlie", "age": 19, "grade": "A+"}
# ]
# with open("students.pkl", "wb") as file:
#     pickle.dump(students, file)
# print(" Student records serialized to students.pkl")
# with open("students.pkl", "rb") as file:
#     loaded_students = pickle.load(file)
# print("\n Loaded Student Records:")
# for student in loaded_students:
#     print(student)



# area_module/
#     __init__.py
#     shapes.py
# use_shapes.py


# import math
# def area_circle(radius):
#     return math.pi * radius ** 2

# def area_rectangle(length, width):
#     return length * width

# def area_triangle(base, height):
#     return 0.5 * base * height
# from area_module import shapes

# print("Circle area (r=5):", shapes.area_circle(5))
# print("Rectangle area (4x6):", shapes.area_rectangle(4, 6))
# print("Triangle area (b=5, h=8):", shapes.area_triangle(5, 8))



# math_operations/
#     __init__.py
#     add.py
#     subtract.py
#     multiply.py
#     divide.py
# use_math.py

# math_operations/add.py

# def add(a, b):
#     return a + b

# math_operations/subtract.py

# def subtract(a, b):
#     return a - b

# math_operations/multiply.py

# def multiply(a, b):
#     return a * b

# math_operations/divide.py

# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b

# use_math.py

# from math_operations import add, subtract, multiply, divide

# print("Add:", add.add(5, 3))
# print("Subtract:", subtract.subtract(10, 4))
# print("Multiply:", multiply.multiply(7, 6))
# print("Divide:", divide.divide(8, 2))



# task 29 :

# from functools import reduce
# numbers = [1, 2, 3, 4, 5, 6]
# doubled = list(map(lambda x: x * 2, numbers))
# evens = list(filter(lambda x: x % 2 == 0, doubled))
# total_sum = reduce(lambda x, y: x + y, evens)
# print("Original list:", numbers)
# print("Doubled:", doubled)
# print("Even numbers only:", evens)
# print("Sum of even numbers:", total_sum)



# task 30:

# import re
# import time
# from functools import wraps
# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
#     return bool(re.match(pattern, email))
# print("Email validation:")
# print(validate_email("test@example.com"))  
# print(validate_email("invalid-email"))     
# print()


# def extract_phone_numbers(text):
#     pattern = r'\+?\d[\d\s-]{7,}\d'
#     return re.findall(pattern, text)
# text_with_numbers = "Call me at +1 234-567-8901 or 9876543210."
# print("Extracted phone numbers:")
# print(extract_phone_numbers(text_with_numbers))
# print()


# def replace_word(text, old_word, new_word):
#     return re.sub(rf'\b{old_word}\b', new_word, text)
# sentence = "Python is great. I love Python."
# print("Replaced text:")
# print(replace_word(sentence, "Python", "Java"))
# print()


def log_execution_time(func):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def sample_function():
    time.sleep(1)
    print("Function executed.")

sample_function()
print()


def require_permission(permission):
    def decorator(func):
        
        def wrapper(user_permissions, *args, **kwargs):
            if permission in user_permissions:
                return func(user_permissions, *args, **kwargs)
            else:
                print("Permission denied.")
        return wrapper
    return decorator


def delete_data(user_permissions):
    print("Data deleted.")


user1_permissions = ["admin", "editor"]
user2_permissions = ["viewer"]

delete_data(user1_permissions) 
delete_data(user2_permissions)  

