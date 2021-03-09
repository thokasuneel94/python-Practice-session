# super() function:
# super() function is a predefined function in python
# by using super() function we can call,
# super class constructor
# super class variable
# super class method

# calling super class constructor from child class constructor
class A:
    def __init__(self):
        print("super class A constructor")
class B(A):
    def __init__(self):
        print("child class B constructor")
        super().__init__()
b=B()
# super and sub classes having same method name, by using super() function child class is accessing super class method
class A:
    def m1(self):
        print("super class A m1 method")
class B(A):
    def m1(self):
        print("child class B m1 method")
        super().m1()
b=B()
b.m1()
# super and sub classes having same variable name, by using super() function child class is accessing super class variable
class A:
    x=10
    def m1(self):
        print("super class A m1 method")
class B(A):
    x=20
    def m1(self):
        print("child class x variable",self.x)
        print("super class x variable",super().x)
b=B()
b.m1()
# calling super class constructor and method from child class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class Employee(Person):
    def __init__(self,name,age,eno,eaddress):
        super().__init__(name,age)
        self.eno=eno
        self.eaddress=eaddress
    def display(self):
        super().display()
        print("employee number:",self.eno)
        print("employee address:",self.eaddress)
e=Employee("anil",27,1234,"hyderabad")
e.display()
# calling method of a specific super class:
# classname.methodname(self)
# super(classname, self).methodname

# classname.methodname(self):
class A:
    def m1(self):
        print("m1 method from A class")
class B(A):
    def m1(self):
        print("m1 method from B class")
class C(B):
    def m1(self):
        print("m1 method from C class")
class D(C):
    def m1(self):
        print("m1 method from D class")
class E(D):
    def m1(self):
        A.m1(self)
e=E()
e.m1()
# super(classname,self).methodname
class A:
    def m1(self):
        print("m1 method from A class")
class B(A):
    def m1(self):
        print("m1 method from B class")
class C(B):
    def m1(self):
        print("m1 method from C class")
class D(C):
    def m1(self):
        print("m1 method from D class")
class E(D):
    def m1(self):
        super(D,self).m1()
e=E()
e.m1()
# different cases for super() function:
# case1:
# by using super() function we cannot access parent class instance variable from child
#class P:
    #def __init__(self):
        #self.a=20
#class C(P):
    #def m1(self):
        #print(super().a)
#c=C()
#c.m1()    AttributeError

# from child if we want to access parent class instance variable then we should use self only
class P:
    def __init__(self):
        self.a=30
class C(P):
    def m1(self):
        print(self.a)
c=C()
c.m1()
# case2:
# by using super() function we can access parent class static variables
class P:
    a=40
    def m1(self):
        print("m1 method from P class")
class C(P):
    def m2(self):
        print(super().a)
c=C()
c.m2()
# case3:
# from child class constructor, we can access parent class
# instance method
# class method
# static method
class P:
    def __init__(self):
        print("P class constructor")
    def m1(self):
        print("m1 instance method from P class")
    @classmethod
    def m2(cls):
        print("m2 class method from P class")
    @staticmethod
    def m3():
        print("m3 static method from P class")
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c=C()
# from child class instance method, we can access parent class
# instance method
# class method
# static method
class P:
    def __init__(self):
        print("P class constructor")
    def m1(self):
        print("m1 instance method from P class")
    @classmethod
    def m2(cls):
        print("m2 class method from P class")
    @staticmethod
    def m3():
        print("m3 static method from P class")
class C(P):
    def __init__(self):
        print("child class constructor")
    def m(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c=C()
c.m()
# case4:
# by using super() function we cannot access parent class instance method and constructor from child class classmethod
#class P:
    #def __init__(self):
        #print("P class constructor")
    #def m1(self):
        #print("m1 instance method from P class")
    #@classmethod
    #def m2(cls):
        #print("m2 class method from P class ")
    #@staticmethod
    #def m3():
        #print("m3 static method from P class")
#class C(P):
    #@classmethod
    #def m(cls):
        #super().__init__()
        #super().m1()
#c=C()
#c.m()    error

# by using super() function we can access parent class static method and classmethod from child class classmethod
class P:
    def __init__(self):
        print("P class constructor")
    def m1(self):
        print("m1 instance method from P class")
    @classmethod
    def m2(cls):
        print("m2 class method from P class")
    @staticmethod
    def m3():
        print("m3 static method from P class")
class C(P):
    @classmethod
    def m(cls):
        super().m2()
        super().m3()
c=C()
c.m()
# case6:
# from class method of child class, how to access parent class instance method and constructors
class P:
    def __init__(self):
        print("P class constructor")
    def m1(self):
        print("m1 instance method from P class")
    @classmethod
    def m2(cls):
        print("m2 class method from P class")
    @staticmethod
    def m3():
        print("m3 static method from P class")
class C(P):
    @classmethod
    def m(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
c=C()
c.m()


