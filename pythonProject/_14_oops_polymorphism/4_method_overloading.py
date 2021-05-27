# method overloading:
# if two methods having same name but different type of arguments then those methods are said to be overloaded method
class Test:
    def m1(self):
        print("no_arg method")
    def m1(self,a):
        print("one_arg method")
    def m1(self,a,b):
        print("two_arg method")
t=Test()
t.m1(10,20)
# with default arguments
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum of three numbers:",a+b+c)
        elif a!=None and b!=None:
            print("the sum of two numbers:",a+b)
        else:
            print("please provide two or three arguments")
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()
# with variable number of arguments
class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print("the sum:",total)
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()
