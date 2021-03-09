# method resolution order:
# in multiple inheritance scenario, initially any specific attribute or method will be searched in the current class
# in current class if not found, then next search continues into parent classes in depth-first left to right fashion
# searching in this order is called method resolution order(MRO)
# execution:  classname.mro()
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
#
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
c=C()
c.m1()
print(C.mro())
#
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m2(self):
        print("m2 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
c=C()
c.m1()
print(C.mro())
#
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
d=D()
d.m1()
print(D.mro())
#
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m2(self):
        print("m2 from D")
d=D()
d.m1()
print(D.mro())
#
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m2(self):
        print("m2 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m2(self):
        print(" m2 from D")
d=D()
d.m1()
print(D.mro())
#
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("")


