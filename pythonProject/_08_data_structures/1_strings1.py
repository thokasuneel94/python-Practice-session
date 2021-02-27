# accessing string characters:
# by using index
# by using slice operator

# by using index

# accessing string index by using positive ,negative values and out of index
s="ravi"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
# print(s(7))        indexerror
# wap to accept some string from the keyboard and print all characters with index
s=input("enter some string:")
i=0
for x in s:
    print("the characters present at positive index:{}and at negative index:{}is:{}".format(i,i-len(s),x))
    i=i+1
# printing character by character from string by using for loop
s="suneel"
for x in s:
    print(x)

# by using slice operator
# nameofthestring[beginindex:endindex:step]
s='0123456789'
print(s[::])
print(s[0::])
print(s[::-1])
print(s[2:8:1])
# print(s[2:8:-1])      ''
print(s[-1:-6:-1])
print(s[2:-5:1])
print(s[:0:-1])
# print(s[1:6:-2])      ''
# print(s[0:-5:-5])     ''
print(s[-5:0:-9])
# print(s[2:-1:-1])     ''
# print(s[2:-5:-1])     ''
# wap to access each character of string in forward direction and backward direction
s=input("enter some string:")
n=len(s)
print("data in forward direction")
i=0
while i<n:
    print(s[i],end='')
    i=i+1
print()
print("data in backward direction")
i=n-1
while i>=0:
    print(s[i],end='')
    i=i-1
print()
print("data in backward direction")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1
print()
# mathematical operators on string objects:
# +
# *

# +
a='sunny'
b='leone'
print(a+b)         # both are strings only
# a='sunny'
# b=20
# print(a+b)       typeerror      one is string another is int   typeerror

# *
a='siva'
print(a*3)
print(3*a)
# length of the string:
a='sunny'
print(len(a))
# membership operators on string object:
# in
# not in
s='anil'
print('a' in s)
print('a' not in s)
print('l' in s)
print('n' not in s)
print('d' not in s)
# to find sub string in main string
main=input("enter main string:")    # "core python  very easy"
sub=input("enter sub string:")      # very
if sub in main:
    print(sub,"is found in main string")        # very is found in main string
else:
    print(sub,"is not found in main string")
# comparision operators on string objects:
# ==
# !=
# <
# >
s1=input("enter first string:")
s2=input("enter second string:")
if s1==s2:
    print("both strings are equal")
else:
    print("both are not same")

s1=input("enter first string:")
s2=input("enter second string:")
if s1<s2:
    print("s1 is smaller than s2")
else:
    print("s1 is greater than s2")
# removing spaces in starting and ending of the string
s="   sunny  "
print("with spaces the length of s is",len(s))
x=s.strip()
print("after removing spaces the length of s is",len(x))













