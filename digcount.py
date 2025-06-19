num = int(input("Enter a number: "))
target = int(input("Enter the digit to count: "))
count = 0
temp = num

while temp > 0:
    digit = temp % 10
    if digit == target:
        count += 1
    temp //= 10

print(f"The digit {target} appears {count} times.")