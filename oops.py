# 1 // class:

# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d \nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()


## delete the object:=

# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d \nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name
# emp.display()


# 2 // object:

# The object is the entity that has state and behaviour.

# class Car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=Car("Toyota",2016)
# c1.display()


# 3 // method:

# 3.1 constructor:=parameteraised=
# The method __init__() simulates the constructor of the class.

# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID:%d \nName:%s"%(self.id,self.name))
# emp1=Employee("John",101)
# emp2=Employee("David",102)
# emp1.display()
# emp2.display()

# 3.2 constructor:=non parameteraised=

# class Student:
#     def __init__(self):
#         print("This is non parameterised constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("John")


