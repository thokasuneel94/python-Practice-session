# class method:
# @classmethod
# def m1(cls):
#    cls.x
# call the class method either by using classname or by using object reference
#
class Pizza:
    radius=700
    @classmethod
    def get_radius(cls,b):
        print("getting radius for pizza1")
        return cls.radius
print(Pizza.get_radius(70))
pizza1=Pizza()
print(pizza1.get_radius(90))
#
class Student:
    marks=100
    @classmethod
    def get_marks(sunny,b):
        print("getting marks for student1")
        return sunny.marks
print(Student.get_marks(70))
s=Student()
print(s.get_marks(80))
#
class Pizza:
    radius=500
    size=400
    @classmethod
    def get_radius(cls,b):
        print("getting radius for pizza1")
        return cls.radius
    @classmethod
    def wish(cls,b):
        print("getting size for pizza2")
        return cls.size
print(Pizza.get_radius(60))
pizza1=Pizza()
print(pizza1.get_radius(80))
print(Pizza.wish("suresh"))
pizza2=Pizza()
print(pizza2.wish("ramesh"))
#
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
Animal.walk('dog')
Animal.walk('cat')
# write a program to track the number of objects created for a class
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noofobjects(cls):
        print("the number of objects created:",cls.count)
t1=Test()
t2=Test()
Test.noofobjects()
t3=Test()
t4=Test()
t5=Test()
t5.noofobjects()
