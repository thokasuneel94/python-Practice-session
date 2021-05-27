class Duck:
    def talk(self):
        print("quack......quack")
class Cat:
    def talk(self):
        print("moew......moew")
class Dog:
    def talk(self):
        print("bow......bow")
def animal(var):
    var.talk()
duck=Duck()
cat=Cat()
dog=Dog()
animal(duck)
animal(cat)
animal(dog)
#
class Duck:
    def talk(self):
        print("quack......quack")
class Cat:
    def talk(self):
        print("meow......meow")
class Dog:
    def bark(self):
        print("bow......bow")
def animal(var):
    if hasattr(var,"talk"):
        var.talk()
    elif hasattr(var,"bark"):
        var.bark()
duck=Duck()
cat=Cat()
dog=Dog()
animal(duck)
animal(cat)
animal(dog)






