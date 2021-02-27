# wap to reverse the given string:
# by using slice operator:
s=input("enter some string:")
print(s[::-1])
# by using reversed():
s=input("enter some string:")
for x in reversed(s):
    print(x,end='')
#
s=input("enter some string:")
print(''.join(reversed(s)))
# by using while loop
# input= sunny leone sexy
# output=yxes enoel ynnus
s=input("enter some string:")
n=len(s)
i=n-1
while i>=0:
    print(s[i],end='')
    i=i-1
print()
#
s=input("enter some string:")
n=len(s)
i=n-1
output=''
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
# input:sunny leone sexy
# output:sexy leone sunny
#s=input("enter some string:")
#l=s.split()
#l1=[]
#i=len(s)-1
#while i>=0:
    #l1.append(l[i])
   # i=i-1
#output=''.join(l1)
#print(output)
# input:sunny leone sexy
# output:ynnus enoel yxes
s=input("enter some string:")
l=s.split()
l1=[]
for x in l:
    l1.append(x[::-1])
output=''.join(l1)
print(output)
# which characters are there at even index positions and odd index positions
# by using slice operator
s=input("enter some string:")
print("characters at even index positions:",s[::2])
print("characters at odd index positions:",s[1::2])
# by using while loop
s=input("enter some string:")
print("the characters at even index positions")
i=0
while i<len(s):
    print(s[i],end=',')
    i=i+2
print()
print("the characters at odd index positions")
i=1
while i<len(s):
    print(s[i],end=',')
    i=i+2
print()
# wap to remove duplicates present in the string
#
s=input("enter some string:")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)
#
s=input("enter some string:")
print(''.join(set(s)))
# find the number of occurences of each character
s=input("enter some string:")
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
for k,v in d.items():
    print("{} occurs {} times".format(k,v))



