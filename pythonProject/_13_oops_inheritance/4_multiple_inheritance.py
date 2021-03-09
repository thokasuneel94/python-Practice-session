# multiple inheritance:
#
class P1:
    def m1(self):
        print("parent1 method")
class P2:
    def m2(self):
        print("parent2 method")
class C(P1,P2):
    def m3(self):
        print("child method")
c=C()
c.m1()
c.m2()
c.m3()
# parent classes having same method names
class P1:
    def m1(self):
        print("parent1 method")
class P2:
    def m1(self):
        print("parent2 method")
class C(P1,P2):
    def m2(self):
        print("child method")
c=C()
c.m1()
c.m2()
#
class P1:
    def m1(self):
        print("parent1 method")
class P2:
    def m1(self):
        print("parent2 method")
class C(P2,P1):
    def m2(self):
        print("child method")
c=C()
c.m1()
c.m2()