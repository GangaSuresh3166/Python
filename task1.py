# Take user input for grocery items and pantry items
grocery = input("Enter grocery items (comma-separated): ").split(",")
pantry = input("Enter pantry items you already have (comma-separated): ").split(",")

final=[]
for item in grocery:
    if item not in pantry:
        final.append(item)
print("\n Final list of items to buy:")
for item in final:
    print("-",item)

