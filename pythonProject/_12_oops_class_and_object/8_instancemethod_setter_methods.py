# setter method 0r mutator method:
# to set/modify values===>change values
# initialize and access the setter method
class customer:
    def set_name(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
        print(c.name,c.age,c.sal)
    def set_id(self,id,rollno):
        self.id=id
        self.rollno=rollno
        print("setting up values in set_id function")
        print(c.id,c.rollno)
c=customer()
c.set_name("suresh",24,20000)
c.set_id(100,47)
print(c.name,c.age,c.sal)
print(c.id,c.rollno)
#
class Fruit:
    def banana(self,color):
        self.color=color
        print(f.color)
    def mango(self,taste):
        self.taste=taste
        print(f.taste)
f=Fruit()
f.banana("yellow")
f.mango("sweet")
print(f.color)
print(f.taste)







