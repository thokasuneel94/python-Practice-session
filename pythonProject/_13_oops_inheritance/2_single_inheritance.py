# single inheritance:
class A:
    def m1(self):
        print("A class m1 method")
class B(A):
    def m2(self):
        print("child B is derived from A class m2 method")
c=B()
c.m1()
c.m2()
