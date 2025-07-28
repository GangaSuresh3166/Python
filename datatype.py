#string data type*********************


# a ="Hello World"
# print(a[0:9:2])

# a ="Hello World"
# print(a[-1])


# a ="Hello World"
# print(a[::-1])


# ##lower()

# msg='PYTHON IS FUN'
# print(msg.lower())

# ###upper
# msg='python is fun'
# print(msg.upper())






# ##count()
# txt="i love apples,apples are favourt fruit"
# x=txt.count("p")
# print(x)

###find

###*find*88
# msg='python is fun programing language'
# print(msg.find('fun'))


##replace(),...........

# text='bat,ball'
# replaced_text=text.replace('ba','ro')
# print(replaced_text)

#*##
   #list_________
   
   #append****
# num=[10,20,30,40]
# print("before append:",num)
# num.append(50)
# print("after appebnd:",num)

#insert******
# vowel=['a','e','i','u']
# vowel.insert(3,'o')
# print(vowel)


#exetend******
# prime_num=[2,3,5]
# print(prime_num)
# even_num=[4,6,8]
# print(even_num)
# prime_num.extend(even_num)
# print(prime_num)








# a=[]
# b=int(input("enter the num"))
# for i in range(0,b):
#     c=int(input("enter your values"))
#     a.append(c)
# print(a)

###even num list 
# a=[]
# n=int(input("enter the number"))
# for i in range(0,n):
#     if i%2==0:
#         a.append(i)
# print(a)


# ######popp #########3
# prime_num=[2,3,5,7]
# remove=prime_num.pop(2)
# print(remove)
# print(prime_num)

#list 10 numbers and remove the odd numbers using pop
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if i<len(a)-1:
#         if a[i]%2!=0:
#             a.pop(i)
# print("list=",a)
    
    
    
    
    
    
    
    
    
# b=[]    
# while True:
#     print("1.add")    
#     print("2.remove")
#     print("3.exit")

#     choice=int(input("enter your choice"))
#     if (choice == 1):
#         a= int(input("enter a number"))
#         b.append(a)
#         print(b)
#     elif(choice == 2):
#         c=int(input("which number you want to remove"))
#         b.pop(c)
#         print(b)
       
    
# b = []    
# while True:
#     print("1. Add")    
#     print("2. Remove")
#     print("3. Exit")

#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         a = int(input("Enter a number: "))
#         b.append(a)
#         print(b)
#     elif choice == 2:
#         if not b:  # Check if list is empty
#             print("List is empty, cannot remove items")
#             continue
#         print("Current list:", b)
#         c = int(input("Enter the index of the number you want to remove: "))
#         if 0 <= c < len(b):  # Check if index is valid
#             b.pop(c)
#             print("Updated list:", b)
#         else:
#             print("Invalid index!")
#     elif choice == 3:
#         break
#     else:
#         print("Invalid choice!")

# #3del    
# languages=["python","swifft","C++","C","java","rust","R"]
# del languages[1]
# print(languages)
# del languages[-1]
# print(languages)
# del languages[0:2]
# print(languages)

# ##remove

# languages=["python","swifft","C++","C","java","rust","R"]
# languages.remove('python')
# print(languages)

# #reverse
# prime_no=[2,3,5,7]
# prime_no.reverse()
# print('Reversed List:'prime_no)


##repeatation

# list1=[12,14,16,18,20]
# k=list1*2
# print(k)

# ###concatenation

# list1=[12,14,16,18,20]
# list2=[9,10,32,54,86]
# k=list1+list2
# print(k)


# ##leength
# list1=[12, 14, 16, 18, 20, 12, 14, 16, 18, 20]
# a=len(list1)
# print(a)

# ######membership
# list1=[100,200,300,400,500]
# print(600 in list1)
# print(200 in list1)


# ##max
# list1=[103,175,134,185,190]
# print(max(list1))
# ##min
# print(min(list1))

# ##intersection
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7,]
# intersection1=set(list1).intersection(list2)
# print(intersection1)


list1=[1,2,3,5,6,7,8,9,10]
list2=[2,4,6,8,10]
a=[]
for i in range(len(list1)):
 for j in range(len(list2)):
    if list1[i]==list2[j]:
        a.append(list1[i])
print(a)