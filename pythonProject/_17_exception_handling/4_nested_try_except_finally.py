# nested try-except-finally blocks:
# we can take try-except-finally blocks inside try block
# we can take try-except-finally blocks inside except block
# we can take try-except-finally blocks inside finally block
# case1:
# if no exception raised then outer try,inner try,inner finally,outer finally blocks will get executes
try:
    print("outer try block")
    try:
        print("inner try  block")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
# case2:
# if an exception raised inside outer try,then outer except blocks is responsible to handle that exception
try:
    print("outer try block")
    print(10/0)
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
# case3:
# if an exception raised in inner try block then inner except block is responsible to handle,if it is unable to handle then outer except block is responsible to handle
try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
#
try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except NameError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")




