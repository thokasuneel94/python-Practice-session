# wap to print the number of lines,words and characters present in the given file
import os,sys
fname=input("enter file name:")
if os.path.isfile(fname):
    print("file exist",fname)
    f=open(fname,'r')
else:
    print("file doesn't exist")
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("the number of lines:",lcount)
print("the number of words:",wcount)
print("the number of characters:",ccount)