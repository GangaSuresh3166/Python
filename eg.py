mark=float(input("Enter your mark:"))
if(mark<=100 and mark>90):
    print("grade=A")
elif(mark<=90 and mark>80):
    print("grade=B")
elif(mark<=80 and mark>70):
    print("grade=C")
elif(mark<=70 and mark>60):
    print("grade=D")
elif(mark>100):
    print("invalid")
else:
    print("failed")
