# functions programs:
def f1():
    """core python programming"""
    print("good evening")
f1()

"""core python programming"""
def f1():
    print("good morning")
f1()

def f1(name):
    print("hello",name,"good evening")
f1("sunny")
def wish(name):
    print("good morning:",name)
    print("good morning:",name)
    print("good morning:",name)
    print("good morning:",name)
wish("sunny")
wish("bunny")
wish("chinny")
def f1():
    print("good evening")
    print("good evening")
    print("good evening")
f1()

def f1():
    print("good morning")
    print("good morning")
    print("good morning")
f1()
f1()
f1()
f1()

def f1(name):
    print("hello",name,"good evening")
f1("sunny")
f1("leone")
# find square of the number
def square(x):
    print("the square of {} is: {}".format(x,x*x))
square(20)
square(10)
# add two numbers
def add(a,b):
    return a+b
result=add(10,20)
print("the sum is:",result)
print("the sum is:",add(100,200))

def f1():
    print("hello")
print(f1())               # in this not used return type, that default return value is None type.

# whether the given number is even or odd.
def evenodd(n):
    if n%2==0:
        print("{} number is even".format(n))
    else:
        print("{} number is odd".format(n))
evenodd(10)
evenodd(11)
evenodd(10.5)
# to find factorial of given number.
def fact(n):
    result=1
    while n>=1:
        result=result*n
        n=n-1
    return result
print(fact(5))
def fact(n):
    result=1
    while n>=1:
        result=result*n
        n=n-1
    return result
for i in range(1,6):
    print("the factorial of {} is: {}".format(i,fact(i)))
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("the sum:", x)
print("the sub:", y)
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print(type(t))
print("the results are:")
for x in t:
    print(x)

# types of variables:
# global variables
# local variables
# global variables:
# the variable which is declared outside of the function which is available for all modules.
a=10
def f1():
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()                    # global variables available for all functions
# local variables:
# the variable which is declared inside of the function
def f1():
    a=10
    print("f1:",a)
f1()
# def f1():
#    a=20
#    print("f1:",a)
# def f2():
#    print("f2:",a)
# f1()
# f2()                 # local variables available only that particular function
a=10
def f1():
    a=777
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()
# global keyword:
# to make global variable  to the function so that we can perform our required modifications.
# to declare global variables inside function.
#
a=10
def f1():
    global a
    a=777
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()
#
a=10
def f1():
    global a
    a=777
    print("f1:",a)
def f2():
    print("f2:",a)
f2()
f1()
# def f1():
#   global a
#    a=777
#    print("f1:",a)
# def f2():
#    print("f2:",a)
# f2()
# f1()          nameerror
def f1():
    global a
    a=777
    print("f1:",a)
def f2():
    global a
    a=888
    print("f2:",a)
def f3():
    print("f3:",a)
f1()
f2()
f3()
def f1():
    global a
    a=777
    print("f1:",a)
def f2():
    global a
    a=888
    print("f2:",a)
def f3():
    a=999
    print("f3:",a)
f1()
f2()
f3()
# global and local variable names same
a=10
def f1():
    a=20
    print(a)
    print(globals()['a'])
f1()






