# a=set()
# print(type(a))

# set1={1,6,4,'abc'}
# print(type(a))

# Days=set(["monday","tuesday","wednesday","thursday"])
# print(Days)
# print(type(Days))
# for i in Days:
#     print(i)

# Adding values to set=

#use add()method to add single values:
# months=set({"january","february","march","april","may","june"})
# print(months)
# months.add("july")
# print(months)

# use update()method to add multiple values:
# months=set({"january","february","march","april","may","june"})
# print(months)
# months.update(["july","august"])
# print(months)

#removing values in set=

#using discard()method if the item does not exist in the set then the set remain unchanged no any error occurs:
# months=set({"january","february","march","april","may","june"})
# print(months)
# months.discard("july")
# print(months)

#using remove()method if the item does not exist in the set an error will occur:
# months=set({"january","february","march","april","may","june"})
# print(months)
# months.remove("may")
# print(months)

# python operations=

#union-two sets is calculated by using(|)pipe operator.
# The union of the two sets contains all the items that are present in both the sets:
# Days1={"monday","tuesday","wednedsay","thursday"}
# Days2={"friday","saturday","sunday"}
# print(Days1|Days2)

#intersection-two sets is calculated by using(&)pipe operator.
# The union of the two sets gives the set of the elements that common in both sides:
# Days1={"monday","tuesday","wednedsay","thursday"}
# Days2={"monday","tuesday","sunday","friday"}
# print(Days1&Days2)

# example programs:

# 1
# names=["meenu","megha","archa","meenu","jeena"]
# cand=list(set(names))
# print(cand)

# 2
# numbers=set()
# for i in range(0,5):
#     values=int(input("enter five values:"))
#     numbers.add(values)
# print("unique values are:",numbers)


# 3
# c=set()
# A={"a","e","i","o","u"}
# B=str(input("Enter a sentence:"))
# for i in B:
#     if i in A:
#         c.add(i)
# print("existing vowels are:",c)

# 4

