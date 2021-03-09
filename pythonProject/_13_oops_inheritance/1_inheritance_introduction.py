# inheritance:
# creating new classes from already existing classes is called inheritance
# the existing class is called a super class or base class or parent class
# the new class is called a subclass or derived class or child class

# advantages:

# code reusability
# time taken for application development will be less
# redundancy (repetition) of the code can be reduced

# types of inheritance:

# there are three types of inheritance, they are
# single inheritance
# multilevel inheritance
# multiple inheritance

# single inheritance:

# creating a subclass or child class from a single superclass/parent class is called single inheritance

# multilevel inheritance:

# if a class is derived from another derived class then it is called multilevel inheritance

# multiple inheritance:

# if a child class is derived from multiple superclasses then it is called multiple inheritance


# implementing inheritance:
class One:
    def m1(self):
        print("parent class m1 method")
class Two(one):
    def m2(self):
        print("child class m2 method")
c=Two()
c.m1()
c.m2()



