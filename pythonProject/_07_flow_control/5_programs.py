# check whether entered year is leap year or not
year=int(input("enter some year:"))
if year%4==0:
    print("year is leap",year)
else:
    print("not leap year",year)
# find maximum number
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if (a>b) and (a>c):
    print("maximum number is",a)
elif (b>a) and (b>c):
    print("maximum number is",b)
else:
    print("maximum number is",c)
# find grade of student based on marks>=80-->A+,60-79-->A,50-60-->B,40-50-->C,below35-->FAIL
marks=int(input("enter some marks:"))
if marks>=80:
    print("you get grade A+")
elif marks>=60:
    print("you get grade A")
elif marks>=50:
    print("you get grade B")
elif marks>=40:
    print("you get grade C")
else:
    print("FAIL")


