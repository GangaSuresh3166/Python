s=int(input("Enter a number:"))
b=len(str(s))
print("length:",b)
j=0
a=s
if s>0:
    for i in range(b):
        
            c=(a%10)
            j=(j*10)+c
            a=a//10
    print(j)
else:
    print("not done")


    




