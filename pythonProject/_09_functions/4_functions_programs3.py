# function aliasing:

#
def wish(name):
    print("good morning",name)
greeting=wish
print(id(wish))
print(id(greeting))
wish("siva")
greeting("anil")
#
def wish(name):
    print("hello",name)
greeting=wish
del wish
# wish("rakesh")        nameerror
greeting("sandhya")
#
def wish(name):
    print("how are you",name)
greeting=wish
sunny=greeting
sunny("mahesh")
greeting("kajal")
wish("samantha")

# nested functions:

# function inside another function
def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    inner()
outer()
# inner()    nameerror
#
def f1():
    def inner(a,b):
        print("the sum:",a+b)
        print("the average:",(a+b)/2)
    inner(10,20)
    inner(20,30)
    inner(40,50)
    inner(100,200)
f1()
# a function can return another function:
def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
f1()
f1()
# function decorators:
# input function--->decorator function--->output function with extended functionality
# it convert input function to output function with extended functionality
# decorators help to make our code shorter and more pythonic
# with decorator:
def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny bad morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name,"good morning")
wish("samatha")
wish("murali")
wish("sunny")
wish("mahesh")
#
def smartdivision(func):
    def inner(a,b):
        if b==0:
            print("hello stupid...how we can divide with zero")
        else:
            return func(a,b)
    return inner
@smartdivision
def wish(a,b):
    return a/b
wish(10,2)
wish(10,5)
wish(10,0)
# without decorator:
def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny bad morning")
        else:
            func(name)
    return inner
def wish(name):
    print("hello",name,"good morning")
decorfunction=decor(wish)
wish("ravi")
decorfunction("sunny")
wish("sunny")
decorfunction("siva")
wish("siva")
# decorator chaining:
def decor1(func):
    def inner(name):
        print("first decor function execution")
        func(name)
    return inner
def decor2(func):
    def inner(name):
        print("second decor function execution")
        func(name)
    return inner
@decor1
@decor2
def wish(name):
    print("hello",name,"good morning")
wish("samantha")
# square and double the numbers by using decorator
def square(num):
    def inner():
        x=num()
        return x*x
    return inner
def double(num):
    def inner():
        x=num()
        return 2*x
    return inner
@square
@double
def wish():
    return 10
print(wish())
#
def square(num):
    def inner():
        x=num()
        return x*x
    return inner
def double(num):
    def inner():
        x=num()
        return 2*x
    return inner
@double
@square
def wish():
    return 10
print(wish())

