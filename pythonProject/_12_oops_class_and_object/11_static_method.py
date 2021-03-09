# static method:
# if we are using instance variables====>instance method===>self
# if we are using class/static variables====>class method===>cls
# if we are not using any instance and static variables====>static method===>no self,no cls
#
class Math:
    @staticmethod
    def add(x,y):
        print("the sum:",x+y)
    @staticmethod
    def product(x,y):
        print("the product:",x*y)
    @staticmethod
    def average(x,y):
        print("the average:",(x+y)/2)
Math.add(10,20)
Math.product(10,20)
Math.average(10,20)
# in above program if you don't use any decorator,it is considered as static method
class Math:
    def add(x,y):
        print("the sum:",x+y)
    def product(x,y):
        print("the product:",x*y)
    def average(x,y):
        print("the average:",(x+y)/2)
Math.add(100,200)
Math.product(100,200)
Math.average(100,200)
#
class Test:
    count=0
    def __init__(self):
        Test.count+=1
    @staticmethod
    def getnoofobjects():
        print("the number of objects created:",Test.count)
t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()
Test.getnoofobjects()
#
class Employee:
    a=100
    @staticmethod
    def wish():
        a=80
        print("it will take local variables")
        print(e.a)
        print(Employee.a)
        print("static method initialising")
    @staticmethod   # @staticmethod is your choice
    def run():
        print(e.a)
        print(Employee.a)
        print("run method calling")
e=Employee()
e.wish()
Employee.wish()
e.run()
Employee.run()
