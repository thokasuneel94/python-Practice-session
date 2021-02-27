# instance method:
# define a instance method and calling a instance method
class Employee:
    def wish(self):
        print("hello my name is bunny")
emp1=Employee()
emp1.wish()
emp2=Employee()
emp2.wish()
# initialize and access three parameterized instance method by using object name
class Student:
    def wish(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        print("my name is:",self.name)
        print("my roll number is:",self.rollno)
        print("my marks is:",self.marks)
        print(s1.name)
s1=Student()
s1.wish('munni',20,30)
s2=Student()
s2.wish('danbilzerian',40,100)
print(s1.name)
print(s1.rollno)
print(s1.marks)
print(s2.name)
print(s2.rollno)
print(s2.marks)
# print(self.name)  nameerror
# two parameterized constructor and instance method
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def wish(self):
        print("my name is:",self.name)
        print("my salary is:",self.sal)
emp1=Employee('rani',20000)
emp1.wish()
emp2=Employee('kavitha',30000)
emp2.wish()
emp3=Employee('bavya',40000)
emp3.wish()
# initialize and access constructor and instance method
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print("my name is:",self.name)
        print("my roll number is:",self.rollno)
    def wish(self,marks,age):
        self.marks=marks
        self.age=age
        print("my marks is:",marks)
        print("my age is:",age)
s1=Student('danny',20)
s1.wish(40,29)
s2=Student('tim',30)
s2.wish(100,70)
print(s1.name)
print(s1.rollno)
print(s1.marks)
print(s1.age)
print(s2.name)
print(s2.rollno)
print(s2.marks)
print(s2.age)
# print(Student.marks)    attributeerror
# default constructor in python
class Employee:
    def wish(self):
        print("hello hi how are you")
emp1=Employee()
emp1.wish()
print(dir())
# initialize and accessing i

