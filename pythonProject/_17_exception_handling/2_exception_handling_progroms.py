# exception:
# an unwanted, unexpected event which disturbs the normal flow of the program is called exception
# exception handling concept applicable for runtime errors but not for syntax errors

# handling exceptions by using try and except:

# try block:

# try is a keyword in python
# the code which may raise an exception,that code we need to write inside try block

# except block:

# except is a keyword in python
# the corresponding handling code for exception we need write inside except block

# try-except flow:

# if any exception raised in try block,then only execution flow goes to except block for handling code
# if there is no exception,then execution flow won't go to except block
# syntax:
# try:
#    code which may raise an exception
# except:
#     exception handling code

# handling exception by using try and except,normal termination
print("one")
print("two")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("three")
# no exception,so except block won't execute
print("one")
print("two")
try:
    print("try block")
except ZeroDivisionError:
    print("except block: handling code")
print("three")
# exception inside try block and handling code exists in except block
print("one")
print("two")
try:
    print("try block")
    print(10/0)
except ZeroDivisionError:
    print("except block: handling code")
print("three")
# exception inside try block and handling code not exists in except block
#print("sunny")
#print("bunny")
#try:
    #print("try block")
    #print(10/0)
#except TypeError:
    #print("except block: handling code")  # ZeroDivisionError: division by zero
#print("junny")

# after exception raised in try block,if try block contains any other statements,then those statements won't execute
print("sukumar")
print("samantha")
try:
    print("try block")
    print(10/0)
    print("rest of the code")
except ZeroDivisionError:
    print("except block: handling code")
print("kajal")
# exception raised inside except block
print("one")
print("two")
try:
    print("try block")
except ZeroDivisionError:
    print(10/0)
print("three")
# try and except both blocks raising exceptions
print("one")
print("two")
try:
    print("try block")
    print(10/0)
except ZeroDivisionError:
    print("except block: handling code")
    #print(10/0)     # ZeroDivisionError
print("four")
# normal termination
print("five")
print("six")
try:
    print(10/0)
except ZeroDivisionError:
    print("except block1: handling code")
try:
    print(10/0)
except ZeroDivisionError:
    print("except block2: handling code")
print("seven")
# printing exception information
try:
    print(10/0)
except ZeroDivisionError as z:
    print("handling code:",z)
# try with multiple except blocks
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except ZeroDivisionError:
    print("can't divide with zero")
except ValueError:
    print("please provide int value only")
# multiple catch block
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
# multiple catch block
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
# single except block is handling multiple exceptions
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except (ZeroDivisionError,ValueError)as z:
    print("please provide valid numbers only and problem is:",z)
# default except block
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError:can't divide with zero")
except:
    print("default except:please provide valid input only")
# default except block
try:
    print(10/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("default except")



