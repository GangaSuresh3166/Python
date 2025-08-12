# higher order:

# def greet(name):
#     return f"Hello,{name}"
# def call_func(func,value):
#     return func(value)
# print(call_func(greet,"Python"))


# lambda:

# square=lambda x:x*x
# print(square(5))


# built-in:
# 1.map=

# num=[1,2,3,4]
# squared=list(map(lambda x:x**2,num))
# print(squared)


# words=["apple","banana"]
# lengths=list(map(len,words))
# print(lengths)


# 2.filter=

# num=[1,2,3,4]
# even=list(filter(lambda x:x%2==0,num))
# print(even)


# words=["apple","","banana"]
# none=list(filter(lambda x: x!="",words))
# print(none)


# 3.reduce=

# from functools import reduce
# nums=[1,2,3,4]
# sum_all=reduce(lambda x,y:x+y,nums)
# print(sum_all)


# from functools import reduce
# nums=[1,2,3,4]
# product=reduce(lambda x,y:x*y,nums)
# print(product)


# 4.zip=

# names=["alice","bob"]
# ages=[25,30]
# zipped=list(zip(names,ages))
# print(zipped)


# roll_numbers=[101,102]
# classes=["10th","12th"]
# students=list(zip(roll_numbers,classes))
# print(students)


# 5.enumerate=

# fruits=["apple","banana"]
# for index,fruit in enumerate(fruits):
#     print(index,fruit)


# colors=["red","blue"]
# for i, color in enumerate(colors,start=1):
#     print(f"color {i}:{color}")


# recursion:

def factorial(5):
    if 5 == 0:
        return 1
    else:
        return 5*factorial(5-1)

