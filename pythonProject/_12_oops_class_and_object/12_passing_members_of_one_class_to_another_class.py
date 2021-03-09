# passing members of one class to another class
#
class Student:
    def __init__(self,sname,srollno,smarks):
        self.sname=sname
        self.srollno=srollno
        self.smarks=smarks
    def display(self):
        print("student name:",self.sname)
        print("student roll number:",self.srollno)
        print("student marks:",self.smarks)
class Demo:
    def modify(stud):     # instead stud you can also use s object
        stud.smarks=stud.smarks+20
        stud.display()
s=Student("nagarjuna",19,40)
Demo.modify(s)
#
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("employee number:",self.eno)
        print("employee name:",self.ename)
        print("employee salary:",self.esal)
class Test:
    def modify(emp):
        emp.eno=emp.eno+2
        emp.esal=emp.esal+1000
        emp.ename=emp.ename+"nagachaitanya"
        emp.display()
e=Employee(100,"samantha",10000)
Test.modify(e)
#
class Bank:
    def __init__(self,bname,baccountno,bbrance):
        self.bname=bname
        self.baccountno=baccountno
        self.bbrance=bbrance
    def display(self):
        print("bank name:",self.bname)
        print("bank account number:",self.baccountno)
        print("bank bank brance:",self.bbrance)
class Test:
    def modify(b):
        b.baccountno=b.baccountno+28
        b.display()
b=Bank("sbi",10,"kurnool")
Test.modify(b)


