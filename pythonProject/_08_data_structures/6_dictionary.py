# dictionary data structure :
# we can create dictionary type by using curly braces{}
# list,tuple,set====>only to hold individual objects
# dictionary====> key-value pairs.
# duplicate keys are not allowed
# duplicate values are allowed
# heterogeneous objects are allowed for both keys and values
# insertion order is not preserved
# it is mutable
# it is dynamic(increasing and decreasing)
# index and slice operators not applicable
# d={key1:value1,key2:value2}
# how to create dict:
# d={}
# d=dict()
# d[key]=value
d={}
d[100]='sunny'
d[200]='ravi'
d[300]='anil'
d['rich']='siva'
print(d)
d={'a':'apple','b':'banana','c':'cat'}
print(d)
# how to access elements from the dictionary:
d={'a':'apple','b':'banana','c':'cat'}
print(d['a'])
print(d['b'])
# print(d['z'])          keyerror
# wap to enter name and % of marks in a dictionary and display info on the screen
rec={}
n=int(input("enter number of students:"))
i=1
while i<=n:
    name=input("enter student name:")
    marks=input("enter % of marks:")
    rec[name]=marks
    i=i+1
print("name of student","\t","% of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])
# how to update dictionaries:
d={101:'sunny',102:'ravi',103:'siva'}
print(d)
d[400]='pavan'
print(d)
d[101]='anil'
print(d)      # {101:'anil',102:'ravi',103:'siva',400:'pavan'}
# how to elements from the dictionary:
d=[100:'sunny',200:'ravi',300:'siva']
del d[100]
print(d)
# del d[500]         keyerror
d=[100:'sunny',2c00:'ravi',300:'siva']
print(d)
d.clear()
print(d)         # {}
d=[100:'sunny',200:'ravi',300:'siva']
print(d)
d.clear()
# del d           nameerror
# del d.keys()    syntaxerror
d[777]='sunny'
print(d)
# how to specify multiple values for the single key:
# key-value
# 100--->sunny,ravi,siva
l=['sunny','ravi','siva']
d={100:l}
print(d)
# important functions and methods of dictionary:
# dict() function:
# d=dict(list or set or tuple of tuple)
# d=dict({100:'sunny',200:'ravi'})    it is also possible
d=dict([(100,'sunny'),(200,'ravi'),(300,'siva')])  # with list of tuple by using dict
print(d)
d=dict(((100,'sunny'),(200,'ravi'),(300,'siva')))  # with tuple of tuple by using dict
print(d)
d=dict({(100,'sunny'),(200,'ravi'),(300,'siva')})  # with set of tuple by using dict
print(d)
# d=dict({[100,'sunny'],[200,'ravi'],[300,'siva']})  # with set of list by using dict
# print(d)        typeerror
# d=dict((100,'sunny'),(200,'ravi'))
# print(d)        typeerror
# len():
d=dict(((100,'sunny'),(200,'ravi')))
print(len(d))
# get():
# d.get(key)
d=dict(((100,'sunny'),(200,'ravi')))
print(d.get(100))
# print(d.get(500))     #  None
# d.get(key,defaultvalue)
print(d.get(500,'anil'))   # anil
print(d.get(100,'anil'))   # sunny
# pop(): remove and return
# pop(key)
# d.pop(key)
# d.popitem()
d=dict(((100,'sunny'),(200,'ravi')))
print(d)
# print(d.pop())      typeerror
print(d.pop(100))
print(d)
d=dict(((100,'sunny'),(200,'ravi')))
print(d)
print(d.popitem())
print(d)
d=dict(((100,'sunny'),(200,'ravi')))
print(d)
print(d.popitem())
print(d.popitem())      # {}
print(d)
d=dict(((100,'sunny'),(200,'ravi')))
print(d)
print(d.popitem())
print(d.popitem())
# print(d.popitem())    keyerror
print(d)
# keys():
d=dict(((100,'sunny'),(200,'ravi')))
print(d.keys())
for k in d.keys():
    print(k)
# values()
# items():
d={100:'sunny',200:'ravi',300:'anil'}
l=d.items()
print(l)
d={100:'sunny',200:'ravi',300:'anil'}
for k,v in d.items():
    print(k,'....',v)
# d1=d.copy():   cloning
# d[key]=value  ---->key is already available,old value is replaced with new value
# d.setdefault(k,v):
#  key is not already available, value is added.
# key is already available, value is ignored
d={100:'sunny',200:'ravi',300:'siva'}
print(d.setdefault(100,'anil'))
print(d)
d={100:'sunny',200:'ravi',300:'siva'}
print(d.setdefault(400,'anil'))
print(d)
# update():
# d.update(x):
d={100:'sunny',200:'ravi',300:'siva'}
print(d)
d1={'a':'apple','b'='banana'}
# d2={777:'A',888='B'}
# d.update(d1,d2)
# print(d)      typeerror
d.update(d1)
print(d)
d={100:'sunny',200:'ravi',300:'siva'}
print(d)
d.update([(777,'A')])        # list of tuple
print(d)
d={100:'sunny',200:'ravi',300:'siva'}
print(d)
d.update([(777,'A'),(888,'B')])        # list of tuple
print(d)
# wap to take dictionary from the keyboard and print the sum of values
d=eval(input("enter dictionary:"))
s=sum(d.values())                   # sum() function is in-built function in python
print("the sum:",s)
# wap number of occurences of each letter present in the given string
word=input("enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)

















