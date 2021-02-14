# operators :
# operators in  python, are used to perform mathematical and logical operations.
# the following type of  operators available in python:
# arithmetic operators( +, -, *, /, //, %, ** )
# logical operators( and, or, not )
# comparison(relational) operators( ==, !=, >, >=, <, <= )
# assignment operators( =, +=, -=, *=, /=, //=, **= )
# bitwise operators( &, |, ^, ~, <<, >> )
# membership operators( in, not in )
# identity operators( is, is not )

# arithmetic operators:
# + ---> addition operator
# example
a=10
b=20
print('a+b is', a+b)
a='sunny'
b='3'
print('a+b is', a+b)
# - ---> subtraction operator
a=20
b=10
print('a-b is', a-b)
# * ---> multiplication operator
a=10
b=20
print('a*b is',a*b)
a='sunny'
b=3
print('a*b is', a*b)
a=2
b='sunny'
print('a*b is', a*b)
# / ---> division operator
a=10
b=2
print('a/b is', a/b)                 # output a/b is 5.0 ( quotient with any digits after decimal )
# // ---> floor division operator
a=10
b=2
print('a//b is', a//b)                 # output a//b is 5 ( quotient without any digits after decimal )
# % ---> modulus operator
a=10
b=2
print('a%b is', a%b)                  # output a%b is 0 ( returns remainder after dividing )
# ** ---> exponent operator
a=10
b=2
print('a**b is', a**b)
a=10
b=-2
print('a**b is', a**b)
a=10.5
b=2
print('a+b is', a+b)
print('a-b is', a-b)
print('a/b is', a/b)
print('a//b is', a//b)
print('a%b is', a%b)
print('a*b is', a*b)
print('a**b is', a**b)
# logical operators :
# and --->if both the operands are True, then the condition becomes True, otherwise False.
# or --->if any two operands are True, then the condition becomes True, otherwise False.
# not --->reverse the logical state of its operand.
x=5
print(x>4 and x<6)                  # output is True
print(x>4 and x<3)                  # output is False
print(x<3 and x>4)                  # output is False
print(x>6 and x<3)                  # output is False
a=10
b=20
print('a and b is', a and b)
print('a or b is', a or b)
a=20
b=10
print('a and b is', a and b)
print('a or b is', a or b)
a=10
b=0
print('a and b is', a and b)
print('a or b is', a or b)
a=0
b=10
print('a and b is', a and b)
print('a or b is', a or b)
a=1
b='sunny'
print('a and b is', a and b)
print('a or b is', a or b)
a=0
b='sunny'
print('a and b is', a and b)
print('a or b is', a or b)
x=5
print(x>4 or x<6)                   # output is True
print(x>4 or x<3)                   # output is True
print(x<3 or x>4)                   # output is True
print(x>6 or x<3)                   # output is False
print(10 or 10/0)
a=True
b=False
print('not a is', not a)             # output is not a is False
print('not b is', not b)             # output is not b is True
a=10
b=""
c=0
print('not a is', not a)             # True sa 1, False as 0, empty string as False
print('not b is', not b)
print('not c is', not c)
# comparison operator:
# == ---> equal
x=3
y=5
print('x==y is', x==y)                          # output is False
a=10
b=10
print('a==b is', a==b)                          # output is True
a=10
b=5
c=3
d=7
e=2
print('a==b+b==c+d==e*b is', a==b+b==c+d==e*b)
a=1
b=True
print('a==b is', a==b)
a=10
b=10.0
print('a==b is', a==b)
a=10.1
b=10.10
print('a==b is', a==b)
# != ---> not equal
x=3
y=5
print('x!=y is', x!=y)                           # output is True
a=10
b=20
print('a!=b is', a!=b)                           # output is False
# >, >=, <, <= ---> greater than
a=10
b=20
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a='sunny'
b='ravi'
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a,=b is', a<=b)
a='Sunny'
b='sunny'
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a='sunny'
b='sanny'
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a=True
b=False
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a='True'
b='False'
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a=10
b=20
if(a>b):
    print("a is greater than b")
else:
    print("a is not greater than b")
a=10
b=20
c=30
d=40
print('a<b<c<d is', a<b<c<d)
print('a<b<c>d is', a<b<c>d)
a=10
b=20
c=30
d=3
print('a<b<c>d is', a<b<c>d)
a=10
b=True
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a=10
b=False
print('a>b is', a>b)
print('a>=b is', a>=b)
print('a<b is', a<b)
print('a<=b is', a<=b)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
max=a if a>b>c else b if b>c else c
print("max value:", max)
# assignment operators( =, +=, -=, *=, /=, %=, **=, //= )
x=5
print(x)
x=3
x+=5
print(x)
x=6
x-=9
print(x)
x=7
x*=3
print(x)
x=4
x/=2
print(x)
x=4
x//=2
print(x)
x=4
x**=2
print(x)
# bitwise operator(&, |, ^, ~, <<, >>)
a=4
b=5
print(a&b)
print(a|b)
print(a^b)
print(~a)
a=True
b=False
print(a&b)
print(b&a)
print(b&b)
print(a&a)
print(~a)
a=10
b=2
print(a<<b)
print(a>>b)
a=True
b=2
print(a<<b)
print(a>>b)
a=-10
b=2
print(a<<b)
print(a>>b)
# membership operators( in, not in )
l=[10,20,30]
print(10 in l)
print(10 not in l)
print(60 in l)
print(70 not in l)
s="Hello Learning Python is very very easy!!!"
print("Hello" in s)
print("L" in s)
print("Z" in s)
print("Z" not in s)
print("" in s)
print("l" in s)
print("p" in s)
print("P" in s)
print("o" in s)
# identity operators( is, is not )
a=10
b=10
print(a is b)
print(a is not b)
a="sunny"
b="sunny"
print(a is b)
print(a is not b)
l1=[10,20,30]
l2=[10,20,30]
l2==l3
print(l1 is l2)
print(l1 is not l2)
print(l2 is l3)
print(l2 is not l3)
# operators precedence:
a=30
b=20
c=10
d=5
print((a+b)*c/d)
print((a+b)*(c/d))
print(a+(b*c)/d)








