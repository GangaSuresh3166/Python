
s = input("Enter a string: ")
b = len(s)

j = ""
i = b - 1

while i >= 0:
    j += s[i]
    i -= 1

print("Reversed string:", j)

