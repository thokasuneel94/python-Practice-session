# multilevel inheritance:
class A:
    def m1(self):
        print("parent class m1 method")
class B(A):
    def m2(self):
        print("child class B derived from A class m2 method")
class C(B):
    def m3(self):
        print("child class C derived from B class m3 method")
c=C()
c.m1()
c.m2()
c.m3()
