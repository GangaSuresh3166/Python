# 11/07/2025

# def square(num):
#     return num**2
# object_=square(6)
# print("The square of the given number is:",object_)


# def square(num):
#     print(num**2)
# square(6)


# def a_function(string):
#     return len(string)
# print(a_function("Functions"))
# print(a_function("Python"))


# //types of function:

# 1 with argument with return type=

# def square(num):
#     return num*num
# result=square(5)
# print("Square:",result)

# 2 with argument without return type=

# def greet(name):
#     print("Hello",name+"!")
# greet("Anu")

# 3 without argument with return type=

# def get_message():
#     return"Welcome to Python Programming !."
# msg=get_message()
# print(msg)

# 4 without argument without return type=

# def print_numbers():
#     for i in range(1,6):
#         print(i)
# print_numbers()


# //function arguments:

# 1. default arguments=

# def function(n1,n2=20):
#     print("number 1 is",n1)
#     print("number 2 is",n2)
# print("Passing only one argument")
# function(30)

# 2. keyword argument=

# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Without using keyword")
# function(n2=50,n1=20)


# // Builtin function

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("John",101,22)   //create the object of the student
# print(getattr(s,'name'))   //prints the attribute name of the object s
# setattr(s,"age",23)        //reset the value of attribute age to 23
# print(getattr(s.'age'))    //prints the modified value of age
# print(hasattr(s,'id'))     //print true if the student contains the attribute with name id
# delattr(s,'age')           //deletes the attribute age
# print(s.age)               //this will give an error since the attribute age has been deleted






# //lambda

# used to define short,single output,anonymous function.
# it can accept number of functions


# 16/07/2025

# //global variable:

# a=10
# def fun():
#     global a
#     b=a+25
#     print(b)
# fun()
# def sample():
#     global a
#     c=a-5
#     print(c)
# sample()

# recursion:

# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)
# print(fact(5))

# 1:

# first,second=0,1
# print(first,second,end=" ")
# for j in range(8):
#     third=first+second
#     print(third,end=" ")
#     first,second=second,third

# //
# def display(v):
#     print(v)
    
# def addition(a,b):
#     ans=a+b
#     display(f"sum of {a} and {b} is {ans}")
# def substraction(a,b):
#     ans=a-b
#     display(f"substarction of {a} and {b} is {ans}")

# def multtiplication(a,b):
#     ans=a*b
#     display(f"multtiplication of {a} and {b} is {ans}")
# def division(a,b):
#     ans=a/b
#     display(f"division of {a} and {b} is {ans}")

# while True:
#     print("1 . ADDITION")
#     print("2 . substraction")
#     print("3 . multtiplication")
#     print("4 . division")
#     print("5.exit")
#     choice =int(input("enter your choice :"))
#     if (choice == 1):
#         a=int(input("enter a number"))
#         b=int(input("enter the second num"))
#         addition(a,b)
        
#     elif(choice == 2):
#         a=int(input("enter a num"))
#         b=int(input("enter second num"))
#         substraction(a,b)
#     elif(choice == 3):
#         a=int(input("enter a num"))
#         b=int(input("enter second num"))
#         multtiplication(a,b)
#     elif(choice == 4):
#         a=int(input("enter a num"))
#         b=int(input("enter second num"))
#         if(b!=0):
#            division(a,b)
#         else:
#             print("undefined")
#     elif choice==5:
#         print("exiting ......")
#         break


# pattern

# n=6
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

