# overloading:
# we can use same operator or methods for different purposes
# there are three types of overloadings
# operator overloading
# method overloading
# constructor overloading

# operator overloading:

# we can use the same operator for multiple purposes
# + operator for different purposes
print(2+3)               # arithmetic addition
print("sunny"+"leone")   # concatenation
# * operator for different purposes
print(2*3)               # multiplication
print("sunny"*4)         # repetiton
# to overload + operator for our book class object
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
print("the total number of pages:",b1+b2)
# overloading > and <= operators for student class object
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<=other.marks
s1=Student("sunny",100)
s2=Student("anil",200)
print("s1>s2",s1>s2)
print("s1<s2",s1<s2)
print("s1>=s2",s1>=s2)
print("s1<=s2",s1<=s2)
# overload multiplication operator to work on employee object
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days
class TimeSheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
e=Employee("sunny",500)
t=TimeSheet("anil",25)
print("this month salary:",e*t)
#
