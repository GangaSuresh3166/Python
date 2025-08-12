# //Python dictionary is an ordered collection of items.It stores elements in key/value pairs. 
# Here keys are unique identifiers that are associated with each other.


# capital_city={"Nepal":"Kathmandu","Italy":"Rome"}
# print(capital_city)
# for i in capital_city:
#     print(capital_city[i])


# adding/updating elements in dictionary=

# capital_city={"Nepal":"Kathmandu","England":"Londan"}
# print("Initial Dictionary:",capital_city)
# capital_city["Nepal"]="Tokyo"
# print("Updated Dictionary:",capital_city)


# change value of dictionary=
# //we can also use [] to change the value assiciated with a particular key

# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print("Initial Dictionary:",student_id)
# student_id[112]="Stan"
# print("Updated Dictionary:",student_id)


# accessing elements from elements=
# //we use the keys to access their corresponding values

# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print(student_id[111])
# print(student_id[113])


# Removing elements from dictionary=
# //we use the del statement to remove an elements from the dictionary

# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print("Initial Dictionary:",student_id)
# del student_id[111]
# print("Updated Dictionary:",student_id)


# iterating through a dictionary=
# //we can iterate through each key in a dictionary using a for loop.

# squares={1:1,3:9,5:25,7:49,9:81}
# for i in squares:
#     print(squares[i])


# squares={}
# i=0
# for i in range(0,9+1):
#     if i in range(0):
#         squares=i*i
# print(i)


# 11/07/2025


# keys=['name','age','city']
# values=['Alice',30,'New york']
# my_dict=dict(zip(keys,values)) //dict-coverting values to dict, zip-to combine two values, no of values should be equal in all lists
# print(my_dict)