# 1. Right Half Pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end=" ")
#     print()


# 2.left half pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()


# 3.full pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("* ",end=" ")
#     print()


#4.inverted right half pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("* ",end=" ")
#     print()


# 5.inverted left half pyramid:

# n=7
# for i in range(0,n-1):
#     for j in range(0,i):
#       print("* ",end=" ") 
#     print()


# 6.inverted full pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,i):    
#         print(" ",end=" ")
#     for k in range(0,n-i):
#         print("* ",end=" ")
#     print()


# 7. rhombus pattern:

# n=5
# for i in range(0,n):
#     for j in range(0,n+i+1):
#         print(" ",end=" ")
#     for k in range(0,n):
#         print("* ",end=" ")     
#     print()
    
# 8. Diamond pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("* ",end=" ")
#     for m in range(0,n-i):
#         print("* ",end=" ")
#     for l in range(0,i+1):    
#         print(" ",end=" ")
#     print()

# 9.Hourglass pyramid:

# n=5
# for i in range(0,n):
#     for m in range(0,n-i):
#         print("*",end=" ")
#     for l in range(0,i+1):    
#         print(" ",end=" ")
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("* ",end=" ")
    
#     print()


# 10.Hollow Square pattern:

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 11. Hollow full pyramid:

# n=5
# for i in range(0,n):
#   for j in range(0,n-i):
#     print("",end=" ")
#   for k in range(0,n):
#     if(k==0 or k==i or j==0):
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


# 12.Hollow inverted full pyramid:

# n=5
# for i in range(0,n):
#   for j in range(i):
#     print(" ",end=" ")
#   for k in range(2*(n-i)-1):
#     if(k==0 or k==2*(n-i)-2 or i==0):
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


# 13.Hollow diamond pyramid:





#14. floyd's triangle:

# n=4
# a=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(a ,end=" ")
#         a=a+1
#     print()


# 15.Pascal's Triangle:

