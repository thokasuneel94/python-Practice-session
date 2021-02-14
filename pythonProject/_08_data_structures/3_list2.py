# <,<=,>,>= :
x=['Dog','Rat','Cat']
y=['Dat','Cat','Dog']
print(x>y)   # True    # inside of string first elements is same and then compare second elements
x=[10,20,30]
print(10 in x)        # True
print(100 in x)       # False
print(100 not in x)   # True
# clear() function : to remove all elements present in the list
x=[10,20,30]
print(x)
x.clear()
print(x)
# nested : a list inside a list
x=[10,20,[30,40]]
print(x)
print(x[0])
print(x[2])
print(x[2][0])
print(x[2][1])
# nested list by matrix representation
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
print("elements row wise:")
for r in x:
    print(r)
print("elements in matrix style:")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end='')
    print()
# list comprehensions :
# list=[expression for x in sequence if condition]      this is list comprehension
# list=[1,4,9,16,25,36....]
l1=[]
for x in range(1,11):
    l1.append(x*x)
print(l1)
# list=[ expression for x in sequence]
l1=[x*x for x in range(1,11)]
print(l1)
l1=[x+x for x in range(1,11)]
print(l1)
# list=[expression for x in sequence if condition]
l1=[x*x for x in range(1,21)]
l2=[x for x in l1 if x%2==0]
print(l1)
print(l2)
l1=[2**x for x in range(1,11)]
print(l1)
l1=[x*x for x in range(1,11)]
l2=[x for x in l1 if x%2!==0]
print(l1)
print(l2)
l1=[x**2 for x in range(1,11) if (x**2)%2!=0]
print(l1)
words=['Balaiah','Nag','Venkatesh','Chiru']
l=[w[0] for w in words]
print(l)
words=['Balaiah','Nag','Venkatesh','Chiru']
l=[w for w in words if len(w)>6]
print(l)
n1=[10,20,30,40]
n2=[30,40,50,60]
n3=[x for x in n1 if x not in n2]
print(n3)
words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)
# slice operator:
# s='123456789'
# s[begin:end:step]
# step can be either positive or negative
# if step is positive===>forward direction
# begin to end-1
# if step is negative===>backward direction
# begin to end+1
# end should not be -1 or end+1 is 0 the result is always empty string
s='0123456789'
s[0:5:1]
s[4:-1:-1]
s[-7:-2:-1]
s[-4:-1:-1]
s[-2:-3:-2]
s[0:0-1]
s[0:-2:-1]
s[-1:-2:-1]
s[0:-1:-1]
s[::-1]
s[1:7:-1]
# wap to display unique vowels present in the given word
vowels=['a','e','i','o','u','A','E','I','O','U']
word=input("enter some word to search:")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("the number of different vowels present in",word,"is:",len(found))
vowels=['a','e','i','o','u']
word=input("enter some word to search:")
found=[]
for letter in word:
    if letter.lower() in vowels:
        if letter.lower() not in found:
            found.append(letter.lower())
print(found)
print("the number of different vowels present in",word,"is:",len(found))
l1=[10,20,30,40,50]
print(min(l1))
print(max(l1))