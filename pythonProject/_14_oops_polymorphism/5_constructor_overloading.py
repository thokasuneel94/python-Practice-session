# constructor overloading:
# constructor overloading is not possible in python
# if we define multiple constructors then the last constructor will be considered
class Test:
    def __init__(self):
        print("no_arg constructor")
    def __init__(self,a):
        print("one_arg constructor")
    def __init__(self,a,b):
        print("two_arg constructor")
t=Test(10,20)
# with default arguments
class Test:
    def __init__(self,a=None,b=None,c=None):
        print("constructor with 0|1|2|3 number of arguments")
t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)
# with variable number of arguments
class Test:
    def __init__(self,*a):
        print("constructor with variable number of arguments")
t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)




