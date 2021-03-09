# constructors in inheritance:
#
class A:
    def __init__(self):
        print("super class A constructor")
class B(A):
    def m1(self):
        print("child class B m1 method")
b=B()
# child class and super class have constructors
class A:
    def __init__(self):
        print("super class A constructor")
class B(A):
    def __init__(self):
        print("child class B constructor")
b=B()
# call super class constructor from child class constructor
class A:
    def __init__(self):
        print("super class A constructor")
class B(A):
    def __init__(self):
        print("child class B constructor")
        super().__init__()
b=B()
#
