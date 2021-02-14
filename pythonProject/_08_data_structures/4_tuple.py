# tuple data structure:
# tuple is same as list only difference is tuple is immutable.
# read only version of list is nothing but tuple
# insertin order is preserved
# duplicates are allowed
# heterogeneous objects are allowed
# tuple elements  we can represents paranthesis(). parenthesis is optional
t=10,20,30,40
print(type(t))
print(t)
t=(10)
print(type(t))    # int type because single value
t=('A')
print(type(t))    # str type
print(t)
t=('A',)
print(type(t))    # tuple
print(t)
# which are valid tuples:
# t=() # tuple
# t=10,20,30  # tuple
# t=10    # int
# t=10,   # tuple
# t=(10)  # int
# t=(10,)  # tuple
# t=(10,20,30,40)  # tuple
# t=(10,20,30,)    # tuple
# tuple creation:
# empty tuple:
# t=()
# single value tuple:
# t=(10,)
# multi value tuple:
# t=(10,20,30)
# t=10,20,30
# tuple() function:
l=[10,20,30]
t=tuple(l)
print(t)
t=tuple(range(1,11,2))
print(t)
# access elements of tuple:
# by using index
# by using slice operator
t=(10,20,30,40,50)
print(t)
print(t[0])
print(t[1:4:1])
t=tuple('sunnyleone')
print(t)     # ('s','u','n','n','y','l','e','o','n','e')
print(t[0])      # s
print(t[1:4:1])  # ('u','n','n')
# t=(10,20,30)
# t[1]=777    typeerror
# which mathematical operators allowed tuple:
# +
# *
# +
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t1)   # (10,20,30)
print(t2)   # (40,50,60)
print(t3)   # (10,20,30,40,50,60)
# *
t1=(10,20,30)
t2=t1*2
print(t2)     # (10,20,30,10,20,30)
t1=(10,20,30,40)
t2=(10,20,30,40)
t3=t1+t2
print(t3)     # (10,20,30,40,10,20,30,40)
# important functions of tuple:

# len():
t=(10,20,30,40)
print(len(t))    # 4
# count() method:
t=(10,20,30,10,30,10)
print(t.count(10))   # 3
# index() function:
t=(10,20,30,40)
print(t.index(10))   # 0
# print(t.index(90))       ValueError
# sorted():
t=(30,10,50,40,20)
print(sorted(t))    # [10,20,30,40,50] sorted the tuple we get the list
# t.sort()
# print(t)            AttributeError

t=(30,10,50,40,20)
l=sorted(t)
print("tuple:",t)   # (30,10,50,40,20)
print("list:",l)    # [10,20,30,40,50]
t1=(30,10,50,40,20)
t2=tuple(sorted(t1))
print(t1)     # (30,10,50,40,20)
print(t2)     # (10,20,30,40,50)
t1=(30,10,50,40,20)
t2=tuple(sorted(t1,reverse=true))
print(t1)
print(t2)      # (50,40,30,20,10)
t1=(30,10,50,40,20)
print(min(t1))
print(max(t1))
l=[10,20,30,40]
print(min(l))
print(max(l))
s='sunny'
print(min(s))
print(max(s))
s={10,20,30,40}
print(min(s))
print(max(s))
# cmp() is only available in python-2. not in python-3
# cmp(t1,t2)   in python-2
# t1=t2    return 0
# t1<t2    return -1
# t1>t2    return +1
# <,<=,>,>= :
t1=(10,20,30)
t2=(40,50,60)
print(t1<t2)   # True
t1=(10,20,30)
t2=(5,50,60)
print(t1<t2)
# tuple packing and tuple unpacking:
# packing===>grouping into single
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
a=10
b=20
c=30
d=40
l=[a,b,c,d]
print(l)
a=10
b=20
c=30
d=40
s={a,b,c,d}
print(s)
# unpacking
t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c",c,"d=",d)
l=[10,20,30,40]
a,b,c,d=t
print("a=",a,"b=",b,"c",c,"d=",d)
s={10,20,30,40}
a,b,c,d=t
print("a=",a,"b=",b,"c",c,"d=",d)
s='abcd'
a,b,c,d=t
print("a=",a,"b=",b,"c",c,"d=",d)
# tuple comprehension is not supported.
t=(x*x for x in range(1,11))
print(type(t))  # <class 'generator'>
t=(x*x for x in range(1,11))
for x in t:
    print(x)
# wap to take a tuple of numbers from the keyboard and print sum,average.
t=eval(input("enter some tuple of numbers:"))
l=len(t)
sum=0
for x in t:
    sum=sum+x
print("the sum:",sum)
print("the average:",sum/l)
