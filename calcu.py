from calcu1 import  addition, subtraction, multiplication, division

while True:
    print("1 . ADDITION")
    print("2 . subtraction")
    print("3 . multiplication")
    print("4 . division")
    print("5.exit")
    choice =int(input("enter your choice :"))
    if (choice == 1):
        a=int(input("enter a number"))
        b=int(input("enter the second num"))
        print(addition(a,b))
        
    elif(choice == 2):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        print(subtraction(a,b))
    elif(choice == 3):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        print(multiplication(a,b))
    elif(choice == 4):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        if(b!=0):
           print(division(a,b))
        else:
            print("undefined")
    elif choice==5:
        print("exiting ......")
break