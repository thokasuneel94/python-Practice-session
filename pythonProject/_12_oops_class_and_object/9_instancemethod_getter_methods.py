# getter method or accessor method:
# to get the values
# to access the values
#
class customer:
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
c=customer()
c.set_name("nag")
c.set_id(679)
print(c.get_name())
print(c.get_id())
#
class Employee:
    def emp(self,name):
        self.name=name
    def run(self):
        return self.name
    def sun(self,id):
        self.id=id
    def jun(self):
        return self.id
e=Employee()
e.emp("lavanya")
e.sun(198)
print(e.run())
print(e.jun())

# print student name and marks
class Student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n=int(input("enter number of students:"))
for i in range(n):
    s=Student()
    name=input("enter name of student:")
    s.setname(name)
    marks=int(input("enter marks of student:"))
    s.setmarks(marks)
    print("student name is:",s.getname())
    print("your marks are:",s.getmarks())


