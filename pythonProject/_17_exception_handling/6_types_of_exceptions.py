# types of exceptions:
# predefined exceptions or in built exceptions
# user defined exceptions or customized exceptions

# predefined exceptions:
# the exceptions which are raised automatically by python whenever a particular event occurs
# example1:
# print(10/0)    # ZeroDivisionError
# example2:
# x=int("ten")
# print(x)       # ValueError

# user defined exceptions or customized exceptions:
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg     # msg is predefined variable in python and compulsory used
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input("enter age:"))
if age>60:
    raise TooYoungException("plz wait some more time definitely you will get best match soon")
elif age<18:
    raise TooOldException("your age already crossed marriage age no chance of getting marriage")
else:
    print("thanks for registration....you will get match details by mail..")
# raise is a keyword in python


