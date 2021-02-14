# list:
# creation of list objects:
# empty list:
l=[]
print(type(l))
print(l)
# if we know elements already:
l=[10,20,30,40]
print(l)
# with dynamic input
l=eval(input("enter some list:"))
print(l)
# with list() function:
l=list(range(0,10,2))          # list function list()
print(l)
s='sunny'
l=list(s)
print(l)
# split() function:
s="learning python is very easy"
l=s.split()                             # split function  split()--->convert string to list
print(l)
# nested list
l=[10,20,[30,40]]
print(l[1])
print(l[2])
print(l[2][1])
print(l[2][0])
# print(l[10])         indexerrors
# accessing elements of a list:
l=[10,20,30,40,50]
print(l[::])           # list[begin:end:step]
print(l[::2])          # step can be either positive or negative
print(l[::-1])
l=[10,20,[30,40],50,60]
print(l[0:3])
l=[10,20,30]
l[1]=7777
print(l)
# traversing the elements of list:
# the sequential access of each element in the list is called traversing the elements of list.
# by using while loop.
l=[1,2,3,4,5,6,3,4,5,7,8]
i=0
while i<len(l):
    print(l[i])
    i=i+1
# by using for loop.
l=[1,2,3,1,2,3,4,5]
for x in l:
    print(x)
l=[1,2,3,7,8,9,10,1,2,7]
for x in l:
    if x%2==0:
        print(x)
l=["a","b","c","d"]
x=len(l)
for i in range(x):
    print(l[i],"is available at positive index:",i,"and at negative index:",i-x)

# important functions and methods  of list:

# in java only methods can be used.we never going to use functions.
# in python we can use either functions or methods.
# outside of class is function
# if you declare a function inside a class is called methods. calling a method with object reference.
def f1():                       # f1 is function
    print("hello this is function")
class student:
    def info(self):              # info is method
        print("it is method and dont get confuse")
f1()                               # calling a function
s=student()
s.info()                           # calling a method
# len(list). this is function:

l=[10,20,30,40]
print(len(l)

# count(x).this is method:

l=[10,20,30,10,10,10,20,10]
print(l.count(10))
print(l.count(20))

# index(x).this is function:

l=[10,20,30,40,10,20,10,10]
print(l.index(10))  # only first one occupied
print(l.index(20))
# print(l.index(50))      valueerror
# membership operator. in
l=[10,20,30,40,10,20,10,10]
target=int(input("enter the value to search:"))
if target in l:
    print(target,"available and its first occurance is at:",l.index(target))
else:
    print(target,"not available")    # index(50) also get output is 50 not available by using in operator
l=[10,20,30,40,10,20,10,10]
target=int(input("enter the value to search:"))
try:
    print(target,"available and its first occurrence is at:",l.index(target))
except ValueError:
    print(target,"not available")
# manipulating elements of list:
# l.append(element)
l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append('sunny')
print(l)
# wap to add all element to list upto 100 which are divisible by 10.
l=[]
for x in range(101):
    if x%10==0:
        l.append(x)
print(l)
# insert()
# l.insert(index,element)
l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)
l.insert(1,50)
print(l)
l.insert(50,777)
print(l)
l.insert(-10,999)
print(l)
print(l.index(777))
print(l.index(999))
# extend()
l1=["chicken","mutton","fish"]
l2=["kf","rc","fo"]
l1.extend(l2)
print(l1)
print(l2)
l1=[10,20,30,40]
l2=[50,60,70]
l3=l1+l2
print(l1)
print(l2)
print(l3)
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
l1.extend('sunny')         # every character is treated as a element
# l1.append('sunny')       # sunny treated as a single element
print(l1)
# remove() method
l1=[10,20,30]
l1.remove(20)
# l1.remove(40)       valueError
print(l1)
# membership operator. in
l1=[10,20,30,40,50,60,70]
x=int(input("enter element to be removed:"))
if x in l1:
    l1.remove(x)
    print("removed successfully")
    print(l1)
else:
    print("specified element is not available")
# pop() function: remove and returns last element
l1=[10,20,30,40,50,60,70]
print(l1.pop())
print(l1.pop())
print(l1)
# l1=[]
# print(l1.pop())       indexError
# pop(index)    that index value is removed
l1=[10,20,30,40,50,60,70]
print(l1.pop(2))
print(l1)
# print(l1.pop(10))     indexerror
# list objects are dynamic:
# append(),insert(),extend()===>to increase size
# remove(),pop()===>to decrease size

# ordering elements of list:
# reverse() method
l1=[1,2,3,4,5]
l1.reverse()
print(l1)
# sort() method
# according to default natural sorting order:
# numbers===> ascending order
# string objects===>alphabetical
#  in sort() list should  contain only homogeneous elements
l1=[20,5,15,10,0]
l1.sort()
print(l1)
l1=["boy","dog","apple","cat"]
l1.sort()
print(l1)
l1=["Boy","Dog","apple","Cat"]
l1.sort()
print(l1)
# l1=[20,10,"apple","cat"]
# l1.sort()
# print(l1)       typeerror
l1=['10','20','sunny','ravi']
l1.sort()
print(l1)
# to sort in reverse of natural sorting order:
# l1.sort(reverse=True)
l1=[20,5,15,10,0]
l1.sort(reverse=True)     # l1.sort(True)     typeerror
print(l1)
# l1.sort(reverse=False)
l1=[20,5,15,10,0]
l1.sort(reverse=False)
print(l1)
l1=['Dog','Cat','Lion']
l1.sort(reverse=True)
print(l1)
# aliasing
x=[10,20,30,40]
y=x    # aliasing
print(id(x))
print(id(y))
x=[10,20,30,40]
y=x
y[1]=777
print(x)
# shallow copy means if both are pointed in the same object
# deep copy means  different objects
# cloning: different objects
# create cloned objects in two ways
# by using slice operator
# by using copy() method
# by using slice operator
x=[10,20,30,40]
y=x[:]
print(id(x))
print(id(y))
x=[10,20,30,40]
y=x[:]
y[1]=777
print(x)
print(y)
# by using copy() method
x=[10,20,30,40,50]
y=x.copy()
y[1]=999
print(x)
print(y)
# what mathematical operators apply for list objects:
# +
# *
# +  both should be list objects
a=[10,20,30,40]
b=[50,60,70,80]
c=a+b
print(c)
a=[10,20,30,40]
b=[50,60,70,80]
c=a+b
print('a:',a)
print('b:',b)
print('c:',c)
a=[10,20,30,40]
b=[50,60,70,80]
c=a.extend(b)
print('a:',a)
print('b:',b)
print('c:',c)
# a=[10,20,30,40]
# c=a+50
# print(c)   typeerror
a=[10,20,30,40]
c=a+[50]
print(c)
# *
a=[10,20,30,40]
c=a*2
print(c)
# comparing list objects:
x=['Dog','Cat','Rat']
y=['Dog','Cat','Rat']
z=['DOG','CAT','RAT']
print(x==y)
print(x==z)
print(x!=z)
print(x is y)
print(x[0] is y[0])
print(id(x[0]))
print(id(y[0]))
# x==y :
# the number of elements must be equal
# the order should be same
# the contents should be same(including case)
# <,<=,>,>= :
x=[50,20,30]
y=[40,90,100,120,170]
print(x>y)  # it is always compare only first elements of list
x=[50,20,30]
y=[50,90,100,120,170]
print(x>y)     # first elments matched compare second elements
print(x>=y)    # first elements matched compare second elements
x=[50,100,300]
y=[50,90,100,120,170]
print(x>=y)    # first elements matched compare second elements
x=['Dog','Rat','Cat']
y=['Rat','Cat','Dog']
print(x>y)     #  inside of the string first elments are compare