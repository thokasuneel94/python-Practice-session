# data types :
# the type of data stored into a variable or memory is called data type.
# different types of data types :

# there are two types of data types

# built-in data types:

# the data types which already available in python are called built-in data types.
# numeric types(int, float, complex)
# bool(boolean type)
# None
# str
# bytes
# bytearray
# list
# set
# frozenset
# tuple
# dict
# range

# user defined data types:

# the data type which are created by the programmers are called user-defined data types.
# class, module, array etc.

# built-in data types:
# int data type:
# the int data type represents values or numbers without decimal values.
a=20
print(type(a))
print(a)
a=99999999999999999999999
print(type(a))
print(a)
# float data type:
# the float data type represents a number with decimal values.
a=69.6
print(type(a))
print(a)
a=1.2e3
print(type(a))
print(a)
a=2e2
b=2E3
C=2e4
print(a)
print(b)
print(c)
# complex data type:
# the complex data type represents the numbers which is written in the form of a+bj or a+bJ.
# a and b may contain integers or floats.
# a use either decimal, octal, hexa forms.
# b use  decimal form only.
a=10+20j
b=10.5+2.3j
print(a)
print(b)
a=10+20j
b=20+30j
print(a+b)
print(a-b)
print(a*b)
print(a.real)
print(a.imag)
a=0b1111+20j
b=0x77+20j
c=0o22+20j
print(a)
print(b)
print(c)
# a=20+0b111j   print(a)    output is syntaxerror
# bool data type:
# allowed values True and False.
# True as 1, False as 0, empty string as False.
a=True
b=False
print(a)
print(b)
print(a+b)
print(a+a)
print(a<b)
print(a>b)
# str data type:
# a group of characters enclosed within single quotes or double quotes or trible quotes.
s='a'
print(type(s))
print(s)
s='sunny'
print(type(s))
print(s)
s="sunny"
print(type(s))
print(s)
print(len(s))
s='''sunny
       leone'''
print(type(s))
print(s)
s='''madhu sir "python" classes'''
print(s)
s='madhu sir "python" classes'
print(s)
s="sunny"
s[0]
s[1]
s[2]
s[-1]
s[-2]
s[-3]
s[1:4]
s[2:4]
s[1:]
s[:4]
s[:]
s[-4:-1]
s[1:100]
s="corepythonprogramming"
s[1:10]
s[1:10:2]
# bytes data type:
# bytes data type represents group of numbers just like an array.
# bytes data type can store the values which are from 0 to 256.
# bytes data type can not store negative numbers.
# bytes data type is immutable.
x=[10,20,30,40]
b=bytes(x)
print(type(b))
print(b[0])
print(b[1])
print(b[-1])
for x in b:
    print(x)
# b[0]=120        typeerror
# bytes must be in range(0, 256)
# x=[10,20,256,258]     b=bytes(x)     valueerror.
# bytearray data type:
# bytearray data type is same as bytes data type, but bytearray is mutable.
x=[10,20,30,40]
b=bytearray(x)
print(type(b))
print(b[0])
print(b[1])
b[0]=120
for i in b:
    print(i)
# list data structure:
# it is mutable.
# insertion order is preserved.
# duplicates are allowed.
# heterogeneous objects are allowed.
# list can store different data types.
# we can create list data structure by using square brackets[].
l=[]
print(type(l))
l.append(10)
l.append(20)
l.append(30)
l.append(10)
print(l)
l.append('sunny')
print(l)
l.append(None)
print(l)
l[0]
l[-1]
l[1:5]
l.remove(10)
print(l)
s=[10,'sunny',True]
s1=s*2
print(s1)
print(type(s1))
# tuple data structure:
# it is immutable.
# insertion order is preserved.
# duplicates are allowed.
# heterogeneous objects are allowed.
# we create tuple data structure by using parenthesis().
t=(10,'sunny',True,10)
print(type(t))
print(t)
t[0]
t[0:3]
t1=t*2
print(t1)
# range data type:
# it is immutable.
# range data type represents a sequence of numbers.
# we can create a range of values by using range() function.
# range data type values can be print by using for loop.
a=range(10)
print(a)
for i in a:
    print(i)
print(a[0])
print(a[1])
print(a[4])
print(a[0:3])
a=list(range(1,10))
print(a)
a=range(1,10)
print(a[0])
print(a[1])
print(a[4])
# None data type:

# None data type represents an object that does not contain any value.
# if any object having no value, then we can assign that object with None type.
# if any function and method is not returning anything then that method can return None type.
x=None
print(x)
print(type(x))
def f1():
    a=10
def f2():
    print("hello don't be like None")
print(f2())
print(f1())

# set data structure:

# it is mutable.
# insertion order is not preserved.
# duplicates are not allowed.
# heterogeneous objects are allowed.
# we can create set data structure by using curly braces{}.
# set can store same type and different type of elements.
s={10,20,30}
print(type(s))
print(s)
s.add('sunny')
print(s)
s.remove(20)
print(s)
s=set()
for i in range(10):
    s.add(i)
    print(s)
s={'sunny','leone','ravi','siva'}
print(s)
# frozenset data structure:
# frozenset is exactly same as set.but only difference is frozenset is immutable.
s={10,20,30,40}
x=frozenset(s)
print(type(x))
print(x)
# dictionary data structure:

# we can create dictionary type by using curly braces{}:
# dict represents group of elements in the form of key value pairs.
d={100:'sunny',200:'siva',300:'ravi'}
print(type(d))
print(d)
d1={}
print(type(d1))
d1[100]='sunny'
print(d1)
d1[200]='bunny'
print(d1)
d1[300]='chinny'
print(d1)
d1[100]='skinny'
print(d1)








