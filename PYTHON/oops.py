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


# 4 // inheritance:

# 4.1 single = one base class and one derived class

# class Animal:
#     def speak(Self):
#         print("Animal speaking")
# class Dog(Animal):                  //child class Dog inherits the base class Animal
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.speak()
# d.bark()

# 4.2 multilevel = one base class and multiple derived class, one derived class inherits another derived class

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):                 //the child class Dog inherits the base class Animal
#     def bark(self):
#         print("dog barking")
# class DogChild(Dog):              //the child class DogChild inherits the base class Dog
#     def eat(self):
#         print("Eating bread")
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()

# 4.3 multiple = multiple parent class and single derived class

# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def subtraction(self,a,b):
#         return a-b
# class Derived(Calculation1,Calculation2):
#     def Multiplication(self,a,b):
#         return a*b
# d=Derived()
# print(d.summation(10,20))
# print(d.subtraction(50,20))
# print(d.Multiplication(3,10))

# 4.4 hierarchical = single base class and multiple derived class

# class Parent:
#     def func1(self):
#         print("This function is in parent class")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2")
# d=Child1()
# d.func1()
# d.func2()

# c=Child2()
# c.func1()
# c.func3()

# 4.5 hybrid - using morethan one inheritance in a single program

# class Person:
#     def display(self):
#         print("This is the person class")
# class Student(Person):
#     def student_info(self):
#         print("This is the stucent class")
# class Sports:
#     def sports_info(self):
#         print("This is the sports class")
# class SchoolStudent(Student,Sports):
#     def school_student_info(self):
#         print("This is the SchoolStudent")
# s=SchoolStudent()
# s.display()
# s.student_info()
# s.sports_info()
# s.school_student_info()


# 5 // Polymorphism:

# class Bank:
#     def getroi(self):
#         return 10;
# class SBI(Bank):
#     def getroi(self):
#         return 7;
# class ICICI(Bank):
#     def getroi(self):
#         return 8;
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank Rate of Interest:",b1.getroi());
# print("SBI Rate of Interest:",b2.getroi());
# print("ICICI Rate of Interest:",b3.getroi());


# 6 // encapsulation:

#  6.1 protected members=

# class Base: 
# 	def _init_(self): 	
# 		self._a = 2
# class Derived(Base): 
# 	def _init_(self): 		
# 		Base._init_(self) 
# 		print("Calling protected member of base class: ",self._a)  
# 		self._a = 3
# 		print("Calling modified protected member outside class: ",self._a) 
# obj1 = Derived() 
# obj2 = Base() 
# print("Accessing protected member of obj1: ",obj1._a) 
# print("Accessing protected member of obj2: ",obj2._a)

#  6.2 private members=

# class Base: 
#     def __init__(self): 
#         self.a = "Hello"
#         self.__c = "World"
# class Derived(Base): 
#     def __init__(self): 
#         Base.__init__(self) 
#         print("Calling private member of base class: ") 
#         print(self.__c) 
# obj1 = Base() 
# print(obj1.a) 


# 7 // Abstraction:

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound()) 

