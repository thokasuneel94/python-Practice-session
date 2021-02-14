# functions:
# a function can contain group of statements which performs the task.

# function related terminology:

# def keyword
# name of the function
# parenthesis()
# parameters(if required)
# colon symbol:
# method body
# return type(optional)
# after defined a function we need to call the function
# if function is parameterized, then pass the values while calling.

# advantages:

# maintaining the code is an easy way.
# code reusability.

# a function can contain mainly two parts

# defining a function
# calling a function
# write  a function once and calling function multiple times.
# defining a function:

# def keyword is used to define function
# after def keyword we should write name of the function
# after function name, we should write parenthesis()
# after parenthesis we should write colon:
# this parenthesis may contain parameters
# parameters are just like variables which receives the values
# if function having parameters, then we need to provide the values while calling
# function body perform the operations
# before closing the function, function may contain return type

# syntax
# def function_name(parameters):
#       """doc string"""
#       body of the function to perform operation
#       return value(if required)

# calling a function

# after defining a function, we need to call to execute the function
# while calling the function, function name should be match otherwise we will get error


# there are two types of functions:

# pre-defined functions or in-built functions.
# user-defined functions.

# pre-defined or in-built functions:

# the functions which already coming along with installed python software.
# id()
# type()
# input()
# print()
# len()
# eval()
# sorted()

# user-defined functions:

# the functions which are defined by developer as per the requirment.
# types of arguments or parameters:

#

#    body
# f1(10,20)
# a,b are formal parameters or formal arguments
# 10,20 are actual arguments

# positional arguments 
# keyword arguments
# default arguments
# variable length arguments

# positional arguments:

# formal arguments=actual arguments
def sub(a,b):
    print(a-b)
sub(100,50)
sub(50,100)                          # sub(a,b) sub(100,50,200) are not matched

# keyword arguments:

def wish(name,msg):
    print("hello",name,msg)
wish(name="sunny",msg="good morning")
wish(msg="good morning",name="sunny")
wish("sunny",msg="good morning")
# wish(msg="good morning","sunny")     positional arg must be first   # output is error

# default arguments:

def wish(name="guest"):
    print("hello",name,"good evening")
wish("sunny")
wish()
def wish(marks,age,name="guest",msg="good morning"):    # default arg should be last
    print("student name:",name)
    print("student age:",age)
    print("student marks:",marks)
    print("message:",msg)
wish(100,48,"sunny")
wish(age=48,marks=100)
wish(100,age=48,msg="bad morning")

# variable length arguments:

def f1(*n):           # n is tuple
    print("var-arg function")
f1()
f1(10)
f1(10,20)
f1(10,20,30)
f1(10,20,30,40)
# wap to print sum of given numbers. i don't how many numbers i am passing
def sum(*n):
    result=0
    for x in n:
        result=result+x
    print("the sum:",result)
sum()
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)
def sum(name,*n):
    result=0
    for x in n:
        result=result+x
    print("the sum by",name,":",result)
sum("sunny")
sum("ravi",10)
sum("anil",10,20)
sum("siva",10,20,30)
sum("meera",10,20,30,40)
def sum(*n,name):
    result=0
    for x in n:
        result=result+x
    print("the sum by",name,":",result)
sum(name="sunny")
sum(10,name="ravi")
sum(10,20,name="anil")
sum(10,20,30,name="siva")
sum(10,20,30,40,name="meera")

# keyword variable length arguments:

def display(**kwargs):           # kwargs is dict
    print("record information:")
    for k,v in kwargs.items():
        print(k,"......",v)
display(name="sunny",marks=100,age=48,gf="pavani")
display(name="ravi",wife1="navya",wife2="sravani",wife3="sandhya")
def display(**x):
    print("record information:")
    for k,v in x.items():
        print(k,"......",v)
display(name="sunny",marks=100,age=48,gf="pavani")
display(name="ravi",wife1="navya",wife2="sravani",wife3="sandhya")
display(name="partha sarathi",brand1="kf",brand2="rc",brand3="fo")
def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(3,2)
f(25,50,arg4=100)
f(arg4=2,arg1=3,arg2=4)
# f()                             typeerror
# f(arg3=10,arg4=40,20,30)        syntaxerror






