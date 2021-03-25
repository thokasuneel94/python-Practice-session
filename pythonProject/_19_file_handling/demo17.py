# reading data from csv file:
import csv
f=open("std.csv","r")
r=csv.reader(f)
data=list(r)
for line in data:
    for word in line:
        print(word,"\t",end="")
    print()