# the special variable __name__:
# __name__=__main__

def f1():
    if __name__=='__main__':
        print("the code executed directly as a program")
        print("the value of __name__:",__name__)
    else:
        print("the code executed indirectly as a module from some other program")
        print("the value of __name__:",__name__)
f1()