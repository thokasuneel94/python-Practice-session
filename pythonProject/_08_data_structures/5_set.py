# set :
# it is mutable
# insertion order is not preserved
# duplicates are not allowed
# heterogeneous objects are allowed
# we can create set data structure by using curly braces{}
# set can store same data type and different elements
# index and slice operator are not applicable
s={30,10,40,5,20}
# s[0]        typeerror
# s[1:2:1]    typeerror
print(s)                # {5,40,10,20,30}
print(type(s))
# set() function: convert any sequence into set
s=set('suny')
print(s)
s=set('abbaaaab')
print(s)        # {'a','b'}
s=set(range(1,6))
print(s)
l=[10,20,30,40,60]
s=set(l)
print(s)
# s={}  it is not set.it is dictionary
# s=set()  it is set
l=[10,20,10,30,20,30]
s=set(l)
print(s)     # {10,20,30}
# important functions and methods of set:
# add() :
# s={10,20,30}
# s.add(newelement)
s=set()
s.add(10)
s.add(20)
s.add(30)
s.add(40)
print(s)    # {40,10,20,30}
# update() :
# s.update(x,y,z....)       x,y,z...... are sequence
s={10,20,30,40}
l=[50,60,70]
s.update(l)
print(s)
s={10,20,30,40}
l=[50,60,70]
s.update(l,range(1,5),'suny')
print(s)
# copy() method:
s={10,20,30,40}
s1=s.copy()
print(id(s))
print(id(s1))
# pop() : remove and return the element some random element
s={10,20,30,40}
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s)
s={10,20,30,40}
print(s.pop())
print(s.pop())
print(s)
# s={10}
# print(s.pop())       10
# print(s.pop())       keyerror
# remove(x) :
s={10,20,30,40}
s.remove(40)
# s.remove(140)        keyerror
print(s)
# discard(): keyerror is  removed
s={10,20,30,40}
s.discard(40)
s.discard(140)
print(s)
# clear() :
s={10,20,30,40}
print(s)
s.clear()
print(s)
# mathematical operators :
# union() :
# s1.union(s2)  or  s1|s2            different elements print. dplicates are not allowed

s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))
print(s1|s2)
# intersection() :
# s1.intersection(s2)  or  s1&s2     only common elements print

s1={10,20,30,40}
s2={30,40,50,60}
print(s1.intersection(s2))
print(s1&s2)

# difference() :
# s1.difference(s2)   or   s1-s2        returns the elements present in s1 but not in s2
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.difference(s2))
print(s1-s2)
# s1^s2 symmetric_difference       elements  present in s1 but not in s2. elements present in s2 but not in s1
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.symmetric_difference(s2))
print(s1^s2)
# membership operators
# in
# not in
s1=set('anil')
print(s1)
print('d' in s1)
print('z' in s1)
print('a' not in s1)
print('s' not in s1)
# set comprehension:
# s={expression for x in sequence condition}
s={x*x for x in range(1,6)}
print(s)
# wap to eliminate duplicates present in the list
l=eval(input("enter some list of values:"))
s=set(l)
print(s)
l=eval(input("enter some list of values:"))
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)
# wap how to identify vowels and its length
w=input("enter some word:")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("the different vowels present in the given word:",d)
print("the number of different vowels:",len(d))



