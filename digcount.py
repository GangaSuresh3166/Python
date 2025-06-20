i = int(input("Enter a number: "))
j = int(input("Enter the digit to count: "))
a = 0

while i > 0:
    a = i % 10
    if a == j:
        
    i=i// 10

print(f"The digit {target} appears {count} times.")