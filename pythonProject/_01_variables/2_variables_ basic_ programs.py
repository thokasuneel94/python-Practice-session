# variables basic programs :
# casting :
#if you want to specify the data type of a variable, this can be done with casting.

# example
x=int(4)            # x will be 4
y=float(4)          # y will be 4.0
z=str(4)            # z will be '4'
print(x)
print(y)
print(z)

#you can get the data type of a variable with the type() function.

# example
x=4
y="sunny"
print(type(x))
print(type(y))

#string variables can be declared either by using single or double quotes.

# example
x='sunny'        # x will be 'sunny'
print(x)         # output is sunny
x="sunny"        # x will be 'sunny'
print(x)         # output is sunny

# case-sensitive :
#variable name are case-sensitive.


# example
#this will create two variables.

a=4
A=2
#plus and concatenation operation on the variable.
x=10
y=20
print(x+y)          # output is 30
a="sunny"
b="leone"
print(a+b)           # output is sunnyleone
print(a+ " " +b)     # output is sunny leone
'''a=20
b="sunny"
print(a+b)            # output is TypeError
print(b+a)            # output is TypeError
'''
#assign a single value to multiple variables.

a=b=c=d=10
print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))
print(d)
print(id(d))       # a,b,c,d address is same

#assigning different values to multiple variable.

a, b, c=10, 20.0, "sunny"
print(a)
print(b)
print(c)

# find area of rectangle by using length, width and formula variables.

length=20
width=10
formula= length * width
print("the aerea of the  rectangle is",formula,"cm squared.")

# find sum of two numbers.

numone=int(input("enter first number:"))
numtwo=int(input("enter second number:"))
sum=numone+numtwo
print("\nresult =",sum)

# check even or odd number

num=int(input("enter the number"))
if num%2==0:
    print("\nit is an even number")
else:
    print("\nit is an odd number")

# check vowel or consonant.

c=input("enter the character:")
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
    print("\nit is a vowel")
elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print("\n it is a vowel")
else:
    print("\nit is a consonant")

# check prime number or not.


