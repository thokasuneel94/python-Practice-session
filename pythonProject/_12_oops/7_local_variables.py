# local variables:
# the variable which we declare inside of the method is called as local variables
# just for temporary usage we can use local variables
# local variables can access within  the method only,we can not access outside of method
# declaring and accessing local variables
class Demo:
    def m1(self):
        a=40
        print(a)
d=Demo()
d.m1()
# trying to access local variable in out of scope
class Demo:
    def m1(self):
        a=70
        print(a)
   # def m2(self):
       # print(a)       nameerror
       # print(self.a)    attributeerror
d=Demo()
d.m1()
# d.m2()        attributeerror
