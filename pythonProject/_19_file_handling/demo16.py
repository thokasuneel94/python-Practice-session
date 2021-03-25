# handling csv files:
# csv ===>comma seperated values
# as the part of programming, it is very common requirement to write and read data
# write csv files,python provides csv module to handle csv files

# writing data to csv file:
import csv
with open("std.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("enter number of employees:"))
    for i in range(n):
        eno=input("enter employee no:")
        ename=input("enter employee name:")
        esal=float(input("enter employee salary:"))
        eaddr=input("enter employee address:")
        w.writerow([eno,ename,esal,eaddr])
print("total employees data written to csv files successfully")


