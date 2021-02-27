# recursive function:

# a function that calls itself
# find factorial by using recursive function
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(0))
print(factorial(5))
print(factorial(3))

# anonymous functions:

# nameless functions are called anonymous functions
#  instant use(only one time usage)
#  syntax:
# lambda input:expression
# find square of number by using anonymous function
s=lambda x:x*x
print(s(4))
print(s(2))
print(s(6))
print(s(9))
# find sum of given two numbers by using anonymous function
s=lambda a,b:a+b
print("the sum of {} and {} is {}".format(2,4,s(2,4)))
print("the sum of {} and {} is {}".format(20,40,s(20,40)))
# find biggest of two numbers by using anonymous function
s=lambda a,b:a if a>b else b
print("the biggest of {} and {} is {}".format(20,40,s(20,40)))

# filter():

# filter() is in-built function
# syntax:
# filter(function,sequence)
# filter by using function
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
print(type(filter(iseven,l)))
l1=list(filter(iseven,l))    # even
print(l1)
# filter by using lambda
l=[0,5,10,15,20,25,30,35,40]
l1=list(filter(lambda x:x%2==0,l))   # even
print(l1)
l2=list(filter(lambda x:x%2!=0,l))   # odd
print(l2)

# map():
# syntax:
# map(function,sequence)
# map by using function
def double(x):
    return 2*x
l=[1,2,3,4,5,6]
print(type(map(double,l)))
l1=list(map(double,l))          # double
print(l1)
# map by using lambda
l=[1,2,3,4,5,6,7,8]
l1=list(map(lambda x:2*x,l))     # double
print(l1)
l2=list(map(lambda x:x*x,l))     # square
print(l2)
#
l1=[1,2,3,4]
l2=[10,20,30,40]   # l1,l2 have same number of elements is must
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)
# reduce():
# syntax:
# reduce(function,sequence)
# reduce is not in python programs. so import the reduce
from functools import reduce
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)
