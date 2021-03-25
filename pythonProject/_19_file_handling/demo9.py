# reading all lines into list
#
f=open("wish.txt",'r')
list=f.readlines()
print(list)
f.close()
#
f=open("wish.txt",'r')
list=f.readlines()
for x in list:
    print(x,end='')

