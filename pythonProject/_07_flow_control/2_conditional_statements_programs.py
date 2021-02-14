# conditional statements: if, elif, else
name=input("enter name:")
if name=="sunny":
    print("hello sunny good morning")
print("how are you")
name=input("enter name:")
if name=="bunny":
    print("hello bunny good morning")
else:
    print("hello guest good morning")
print("how are you")
brand=input("enter your favourate brand:")
if brand=="rc":
    print("it is childrens brand")
elif brand=="kf":
    print("it is not that much kick")
elif brand=="ko":
    print("it is too light")
elif brand=="fo":
    print("buy one get one free")
else:
    print("other brands are not recommended")
# find biggest of given 2 numbers from the keyboard:
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if n1>n2:
    print("bigger number is:", n1)
else:
    print("bigger number is:", n2)
# find biggest of given 3 numbers from the keyboard:
n1=eval(input("enter first number:"))
n2=eval(input("enter second number:"))
n3=eval(input("enter third number:"))
if n1>n2 and n1>n3:
    print("biggest number is:", n1)
elif n2>n3:
    print("biggest number is:", n2)
else:
    print("biggest number is:", n3)
# check whether the given number is in between 1 and 100 or not:
n=int(input("enter number:"))
if n>=1 and n<=100:
    print("the number n is in between 1 and 100")
else:
    print("the number n is not in between 1 and 100")
#
n=int(input("enter a digit from 0 to 9:"))
if n==0:
    print("zero")
elif n==1:
    print("one")
elif n==2:
    print("two")
elif n==3:
    print("three")
elif n==4:
    print("four")
elif n==5:
    print("five")
elif n==6:
    print("six")
elif n==7:
    print("seven")
elif n==8:
    print("eight")
elif n==9:
    print("nine")
else:
    print("plz enter a number from 0 to 9 only")

