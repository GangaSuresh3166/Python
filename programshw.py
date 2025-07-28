# 1.1 

# def numbers(num):
#     if num==0:
#         return
#     print(num)
#     numebrs(num-1)
# numbers(5)

# def rec(num):
#     if num==1:
#         return num
#     else:
#         return f"{num},{rec(num-1)}"
# n=int(input("enter your number"))
# print(rec(n))


# 1.2

# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
# print("sum of first 3 natural numbers:",sum(3))

# def sum(num):
#     if num==0:
#         return num
#     else:
#         return num+(sum(num-1))
# n=int(input("eneter your number"))
# print(sum(n))


# 1.3

# def sum(num):
#     total=0
#     while num>0:
#         total+=num%10
#         num//=10
#     return total
# print(sum(1234))

# def sum(num):
#     if num<10:
#         return num
#     else:
#         return (num % 10) +sum(num//10)
# n=int(input("eneter your number"))
# print(f"sum of digihits of {n} is {sum(n)}")


# 1.4

# def reverse(s):
#     if len(s)<= 0:  
#         return s
#     else:
#         return reverse(s[1:]) + s[0]  
# string = input("Enter a string: ")
# print(f"Reversed string: {reverse(string)}")




# 2.1

# square=lambda x:x*x
# print(square(5))


# 2.2

# odd_even=lambda x:"even" if x%2==0 else "odd"
# print(odd_even(3))


# 2.3

# maximum=lambda a,b:a if a>b else b 
# print(maximum(10,8))


# 2.4

# lambda_ = lambda s: s.startswith('A')
# print("Start A:", lambda_("Archana"))
# print("Start A:", lambda_("Ganga"))


# 3.1

# def maximum(numbers):
#     return max(numbers)
# nums = [12,88,9,76,102]
# print("Maximum:",maximum(nums))


# 3.2

# def str(s):
#     return s[::-1]
# print("Reversed:", str("hello"))


# 3.3

# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# vowelsss=count_vowels("Hello")
# print("Number of vowels:",vowelsss)


# 3.4

# def palindrome(num):
#     temp=num
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     if temp==rev:
#         print("The number is palindrome")
#     else:
#         print("The number is not palindrome")
# a=int(input="enter the number:")
# palindrome(a)


# 3.5

# def even_numbers(num):
#     even_list=[]
#     for even_numbers in num:
#         if even_numbers % 2==0:
#             even_list.append(even_numbers)
#     return even_list
# number=[1,2,3,4,5,6,7,8]
# print("even numbers:",even_numbers(number))


# 3.6

# def power(b,e):
#     result=1
#     for i in range(0,e):
#         result=result*b
#     if e < 0:
#         return 1 / result
#     return result
# b=int(input("Enter the base:"))
# e=int(input("Enter the exponent:"))
# print(f"{b} raised to the power{e} is {power(b,e)}")


# def power(b,e):
#     if e==0:
#         return 1
#     return b*power(b,e-1)
# print("10^2=",(power(10,2)))  //using recurison


def power(b,e):
    result=1
    for i in range(0,e):
        result=result*b
b=int(input("Enter the base:"))
e=int(input("Enter the exponent:"))
print(f"{b} raised to the power{e} is {power(b,e)}")  //without recurion



