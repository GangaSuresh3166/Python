#// odd or even=
#  def is_even(num):
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# a=int(input("enter the num"))
# is_even(a)


#// factorial=

# def factorial(num):
#     fact=1
#     for k in range(1,num+1):
#         fact=fact*k
#     print("factorial of the number is",fact)
# n=int(input("enetr your num"))
# factorial(n)


#// leap year=

# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(year,"is leap year")
#     else:
#         print(year,"is not leap year")
# a=int(input("enter a year"))
# leap_year(a)
        


#// def display(name,age):
#     print(f"hello my name is {name} iam {age} years old")
# display("ganga",59)



def display(**a):
    print(f"hi {a['name']} welome to {a['course']} course")
    
display(name="ganga",course="python")