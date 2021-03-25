
# else block with try-except-finally:
# else block will be executed if there is no exception inside try
# case1:
# if no exception then try,else and finally blocks will get executed
try:
    print("try block")
except:
    print("except block:handling code")
else:
    print("else block")
finally:
    print("finally block")
# if an exception raised inside try block,then except block will get executed but else block won't executed
try:
    print("try block")
    print(10/0)
except ZeroDivisionError:
    print("except block")
else:
    print("else block")
finally:
    print("finally block")

