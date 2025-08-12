
n=5
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or i==2 or (j==0 and i==1) or (j==n-1 and i==n-4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()