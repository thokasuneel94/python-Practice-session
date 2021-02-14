print(True)
print(False)
print(True==1)
print(False==0)
print(True+True+True)        # output is 3
print(False+True+False)      # output is 1

print(True or True)          # output is True
print(True or False)         # output is True
print(False or True)         # output is True
print(False or False)        # output is False

print(True and True)         # output is True
print(True and False)        # output is False
print(False and True)        # output is False
print(False and False)       # output is False

print(not True)              # output is False
print(not False)             # output is True

a=[1, 2, 3, 4]
print(a)                     # output is [1, 2, 3, 4]
del a[1]
print(a)                     # output is [1, 3, 4]

name=input("enter your name:")
if name=="sunny":
    print("hello sunny")
elif name=="leone":
    print("hello leone")
else:
    print("hello guest")
# for loop:
s="sunny"
for i in s:
    print(i)
# while loop:
i=0
while i<=3:
    i+=1
    print(i, end=" ")              # output is 1 2 3


# continue:
for i in range(10):
    if i%2==0:
        continue
    print(i, end=" ")              # output is 1 3 5 7 9

# break:
l=[10,20,30,40,50]
for i in l:
    if i>40:
        print("not requered")
        break
    print(i)                         # output is 10 20 30 not requered

# pass:
def f1():
    print("hello")
def f2():
    pass
f1()                                 # output is hello
f2()


# in:
s="sunny"
print('u' in s)            # output is True
print('y' in s)            # output is True

# is:
l1=["a","b","c"]
l2=["a","b","c"]
l3=l2
print(l1 is l2)             # output is False       # l1, l2 ids are different.
print(l2 is l3)             # output is True
