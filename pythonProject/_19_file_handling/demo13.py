# check file exists or not
import os,sys
fname=input("enter file name:")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,'r')
else:
    print(" file doesn't exists",fname)
    sys.exit(0)
print("the content of the file is:")
data=f.read()
print(data)

#
import os
fname=input("enter file name:")
if os.path.isfile(fname):
    print("file exist",fname)
    f=open(fname,'r')
    data=f.read()
    print("the content of the file is:")
    print(data)
else:
    print("file doesn't exist",fname)

