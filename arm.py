i = int(input("Enter a number: "))
a=i
j=0
b=len(str(i))
while i!=0:
    r=i%10
    j=j+(r**b)
    i=i//10
if a==j:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

   
