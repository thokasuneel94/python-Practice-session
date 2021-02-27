# instance variables( object level variables ):
# if the value of a variable is changing from object to object
# for every object a seperate copy of instance variables will be created

# declare and initialize the instance variables in the following ways

# by using constructor
# by using instance method
# by using object name

# initialize instance variables inside cconstructor by using self variable
class Employee:
    def __init__(self):
        self.name='suresh'
        self.id=100
        self.sal=20000
emp=Employee()
print(emp.name)
print(emp.id)
print(emp.sal)
print(emp.__dict__)
# initialize instance variables inside instance method by using self variable
class Student:
    def m1(self):
        self.a=10
        self.b=20
        self.c=30
        print(self.a)
        print(self.b)
        print(self.c)
s=Student()
s.m1()
print(s.__dict__)
# initialize instance variables by using object name
class Test:
    def __init__(self):
        print("this is constructor")
    def m2(self):
        print("thi is instance method")
t=Test()
t.m2()
t.a=40
t.b=50
t.c=60
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)
# accessing instance variables
# by using self variable
# by using object name

# accessing instance variables by using self variable
class Employee:
    def __init__(self):
        self.a=10
        self.b=20
        print(self.a)
        print(self.b)
    def m1(self):
        print(self.a)
        print(self.b)
emp=Employee()
emp.m1()
# accessing instance variables by using object name
class Employee:
    def __init__(self):
        self.a=30
        self.b=40
emp=Employee()
print(emp.a)
print(emp.b)
# every object has a seperate copy of instance variable exists
# 1
class Test:
    def __init__(self):
        self.a=10
t1=Test()
t2=Test()
print(t1.a)
print(t2.a)
# 2
class Test:
    def __init__(self):
        self.a=10
t1=Test()
t2=Test()
t1.a=888
print(t1.a)
print(t2.a)

