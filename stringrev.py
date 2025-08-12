text=(input("Enter the string:"))
reverse=""
for i in text:
    reverse=i+reverse 
    #reverse =text[::-1] without builtin
print("reversed string:",reverse)

