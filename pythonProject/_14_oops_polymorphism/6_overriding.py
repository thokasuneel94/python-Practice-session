# overriding:
# overriding concept applicable for both methods and constructors
# method overriding:
class P:
    def property(self):
        print("gold+land+cash+power")
    def marry(self):
        print("sara ali khan")
class C(P):
    def marry(self):
        print("kajal")
c=C()
c.property()
c.marry()
# from overriding method of child class, we can call parent class method also by using super() method
class P:
    def property(self):
        print("gold+land+cash+power")
    def marry(self):
        print("samantha")
class C(P):
    def marry(self):
        super().marry()
        print("lavanya")
c=C()
c.property()
c.marry()
# constructor overriding:
class P:
    def __init__(self):
        print("parent constructor")
class C(P):
    def __init__(self):
        print("child constructor")
c=C()
# to call parent class constructor by using super() method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print("employee name:",self.name)
        print("employee age:",self.age)
        print("employee number:",self.eno)
        print("employee salary:",self.esal)
e1=Employee("sara ali khan",25,1234,200000)
e1.display()
e2=Employee("kajal",29,5678,300000)
e2.display()


