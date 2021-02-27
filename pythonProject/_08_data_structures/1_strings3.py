# changing case of a string:
# upper()
# lower()
# swapcase()
# title()
# capitalize()
s="The Python Classes By Madhu Sir"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
# checking starting and ending part of the string
# nameofthestring.startswith()
# nameofthestring.endswith()
s="learning python is very easy"
print(s.startswith("learning"))
print(s.endswith("easy"))
print(s.startswith("Learinig"))
print(s.endswith("Easy"))
# isalnum(),isalpha(),isdigit(),islower(),isupper(),isspace(),istitle()
print("sunny1234".isalnum())
print("sunny1234".isalpha())
print("sunny".isalpha())
print("sunny".isdigit())
print("1234567".isdigit())
print("ABC".islower())
print("abc".islower())
print("abc123".islower())
print("ABC".isupper())
print("Learning python is very easy".istitle())
print("Learning Python Is Very Easy".istitle())
print("1234".istitle())
print("A123".istitle())
s=input("enter any character:")
if s.isalnum():
    print("alphabet character")
    if s.isalpha():
        print("alphabet character")
        if s.islower():
            print("lower case alphabet character")
        else:
            print("upper case  alphabet character")
    else:
        print("it is a digit")
elif s.isspace():
    print("it is space character")
else:
    print("non space special character")
# formating strings:
name="lavanya"
age=28
salary=10000
print("{}'s age is {} and his salary is {}".format(name,age,salary))
print("{0}'s age is {1} and his salary is {2}".format(name,age,salary))
print("{x}'s age is {y} and his salary is {z}".format(z=salary,x=name,y=age))




