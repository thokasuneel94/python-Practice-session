# static variable:
# if the value of a variable is not changing from object to object
# for all objects will be shared a single copy of static variable

#  static variables accessing with object name and class name
class Student:
    college_name='ANR'
    def __init__(self,name,id):
        self.name=name
        self.id=id
s1=Student('kohli',47)
s2=Student('pant',67)
print("student s1 info" )
print("name is:",s1.name)
print("id is:",s1.id)
print("college name is:",s1.college_name)
print("college name is:",Student.college_name)
print("student s2 info")
print("name is:",s2.name)
print("id is:",s2.id)
print("college name is:",s2.college_name)
print("college name is:",Student.college_name)
# declaring static variables:                  # accessing static variables:
# inside class and out side of the method      #
# inside constructor                           # inside constructor
# inside instance method                       # ionide instance method
# inside class method                          # inside class method
# inside static method                         # inside static method
# declaring static variable inside of the class and outside of the method
class Demo:
    a=40
    def m1(self):
        print("this is method")
d=Demo()
d.m1()
print(Demo.__dict__)
# accessing static variables inside of the class and outside of the method
class Demo:
    a=50
    def m2(self):
        print("this is method")
d=Demo()
d.m2()
print(d.a)
print(Demo.a)
# declaring static variables inside constructor by using class name
class Demo:
    def __init__(self):
        Demo.a=30
d=Demo()
d.__init__()
print(Demo.__dict__)
# accessing static variables inside constructor class name and object name
class Demo:
    def __init__(self):
        Demo.a=40
        print(Demo.a)
        print(d.a)
d=Demo()
d.__init__()
print(d.a)
print(Demo.a)
# acceessing static variables inside constructor by using class name and object name
class Demo:
    a=20
    def __init__(self):
        print(self.a)
        print(Demo.a)
        print(d.a)
d=Demo()
d.__init__()
print(Demo.a)
print(d.a)
# declaring static variables inside instance method by using class name
class Demo:
    def m1(self):
        Demo.a=70
d=Demo()
d.m1()
print(Demo.__dict__)
# accessing static variables inside instance method by using class name and object name
class Demo:
    def m1(self):
        Demo.a=30
        print(Demo.a)
        print(d.a)
d=Demo()
d.m1()
print(d.a)
print(Demo.a)
# accessing static variables inside instance method by using class name and object name
class Demo:
    a=50
    def m2(self):
        print(self.a)
        print(Demo.a)
        print(d.a)
d=Demo()
d.m2()
print(Demo.a)
print(d.a)
# declaring static variables iniside class method by using class name
class Demo:
    @classmethod
    def m1(cls):
        Demo.a=60
d=Demo()
d.m1()
print(Demo.__dict__)
# declaring static variables inside class method by using cls variable
class Demo:
    @classmethod
    def m1(cls):
        cls.a=40
d=Demo()
d.m1()
print(Demo.__dict__)
# accessing static variables inside class method by using class name,cls variable and object name
class Demo:
    @classmethod
    def m1(cls):
        Demo.a=50
        cls.b=20
        print(Demo.a)
        print(cls.b)
d=Demo()
d.m1()
print(Demo.a)
print(d.a)
# print(cls.b)     nameerror
print(d.b)
# accessing static variables inside class method by using class name,cls variable and object name
class Demo:
    a=40
    @classmethod
    def m2(cls):
        print(Demo.a)
        print(cls.a)
        print(d.a)
d=Demo()
d.m2()
print(Demo.a)
# print(cls.a)        nameerror
print(d.a)
# declaring static variables inside static method by using class name
class Demo:
    @staticmethod
    def m1():
        Demo.a=80
d=Demo()
d.m1()
print(Demo.__dict__)
# accessing static variables inside static method vy using class name and object name
class Demo:
    @staticmethod
    def m2():
        Demo.a=90
        print(Demo.a)
        print(d.a)
d=Demo()
d.m2()
print(Demo.a)
print(d.a)
# accessing static variables inside static method by using class name and object name
class Demo:
    a=40
    @staticmethod
    def m1():
        print(Demo.a)
        print(d.a)
d=Demo()
d.m1()
print(Demo.a)
print(d.a)



















