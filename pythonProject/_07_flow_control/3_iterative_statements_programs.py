# iterative statements: for loop, while loop
# for loop
# syntax
# for each element in sequence:
#        do some action
s="sunny leone"
for i in s:
    print(i, end="")
#
s="bunny chinny"
count=0
for x in s:
    count+=1
    print(x, end="")
print("the number of characters:", count)
#
s=input("enter some string:")
i=0
for x in s:
    print("the character present at i index is",x)
    i+=1
#
s=input("enter some string:")
i=0
for x in s:
    if i!=0:
        print("the character present at i index is",x)
    i+=1
for x in range(10):
    print("hello")
for x in range(11):
    print(x)
# 0 to 20 display only odd numbers.
for x in range(21):
    if x%2!=0:
        print(x)
#
for x in range(1,21,2):
    print(x)
#
l=eval(input("enter some list"))
sum=0
for x in l:
    sum=sum+x
print("the sum:",sum)
# while loop:
# syntax
# while condition:
#        body
# print 1 to 10 numbers
x=1
while x<=10:
    print(x)
    x+=1
# sum of first n numbers
n=int(input("enter some number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("the sum of first n numbers is:",sum)
# enter some name from keyboard
name=""
while name!="sunny":
    name=input("enter name:")
print("hello sunny thanks for confirmation")
#
name=""
pwd=""
while (name!='sunny') or (pwd!='python'):
    name=input("enter name:")
    pwd=input("enter password:")
print("hello sunny thanks for confirmation")
# infinite loops:
i=0
while True:
    i=i+1
    print("hello:", i)
# nested loop(loop inside other loop):
for i in range(4):
    for j in range(4):
        print("i={} and j={}".format(i,j))
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
n=int(input("enter number of rows:"))
for i in range(n):
    print('*'*n)
n=int(input("enter number of rows:"))
for i in range(n):
    print('*', end='')
n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
n=int(input("enter number of rows:"))
for i in range(1,n+1):
    print("*"*i)