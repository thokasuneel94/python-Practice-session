# polymorphism:
# polymorphism with class methods:

class India:
    def capital(self):
        print("delhi is the capital of india")
    def language(self):
        print("hindi is the most widely spoken language of india")
    def type(self):
        print("india is a developing country")
class Usa:
    def capital(self):
        print("washington d.c is the capital of usa")
    def language(self):
        print("english is the primary language of usa")
    def type(self):
        print("usa is a developed country")
obj_ind=India()
obj_usa=Usa()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
# polymorphism with inheritance:
class Bird:
    def intro(self):
        print("there are many types of birds")
    def flight(self):
        print("most of the birds can fly but some cannot")
class Sparrow(Bird):
    def flight(self):
        print("sparrows can fly")
class Ostrich(Bird):
    def flight(self):
        print("ostrich can not fly")
obj_bird=Bird()
obj_spr=Sparrow()
obj_ost=Ostrich()
obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()
# polymorphism with a function and objects:
class India:
    def capital(self):
        print("new delhi is the capital of india")
    def language(self):
        print("hindi is the most widely spohen language in india ")
    def type(self):
        print("india is a developing country")
class Usa:
    def capital(self):
        print("washington d.c is the capital of usa")
    def language(self):
        print("english is the primary language of usa")
    def type(self):
        print("usa is a developed country")
def func(ide):
    ide.capital()
    ide.language()
    ide.type()
obj_ind=India()
obj_usa=Usa()
func(obj_ind)
func(obj_usa)
#
class Pycharm:
    def execute(self):
        print("compile")
        print("run")
class Myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=Pycharm()
lap1=Laptop()
lap1.code(ide)
#
class Pycharm:
    def execute(self):
        print("compilling")
        print("running")
class Myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=Myeditor()
lap1=Laptop()
lap1.code(ide)



