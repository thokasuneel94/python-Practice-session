# reading only first 10 characters of file
f=open("wish.txt",'r')
data=f.read(10)
print(data)
f.close()