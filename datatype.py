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








a=[]
b=int(input("enter the num"))
for i in range(0,b):
    c=int(input("enter your values"))
    a.append(c)
print(a)