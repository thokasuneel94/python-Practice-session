# constructor:
# syntax
# def __init__(self):
#    body of the constructor

# define a constructor and executed automatically at the time of object creation
class Employee:
    def __init__(self):
        print("constructor executed automatically at the of object creation")
emp=Employee()
emp.__init__()
emp1=Employee()
emp2=Employee()
emp3=Employee()
# no parameterised constructor used to initialize,all objects with same data
class Employee:
    def __init__(self):
        self.id=2
        print("self.id is:",self.id)
emp1=Employee()
emp2=Employee()
emp3=Employee()
emp1.__init__()
emp2.__init__()
emp3.__init__()
# trying to print self variable inside constructor,internally it represents object representation
class Employee:
    def __init__(self):
        print("only self is poarameter,no other parameters",self)
emp=Employee()
# initialize and access three parameterized constructor
class Employee:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        print("name is:",self.name)
        print("id is:",self.id)
        print("age is:",self.age)
emp1=Employee("sunny",120,20)
emp2=Employee("ravi",200,22)
emp3=Employee("anil",300,26)
emp4=Employee("siva",400,28)
emp3.__init__("jaya",900,40)
emp4.__init__("sony",400,50)
print(emp1.name)
print(emp1.id)
print(emp1.age)
print(emp2.name)
print(emp2.id)
print(emp2.age)
print(emp3.name)
print(emp3.id)
print(emp3.age)
print(emp4.name)
print(emp4.id)
print(emp4.age)







