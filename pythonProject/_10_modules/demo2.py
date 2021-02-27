# import a module
import demo1
print(demo1.x)
print(demo1.y)
demo1.add(10,20)
demo1.product(10,20)

# from demo1 as m import x
# print(x)     syntaxerror

# module aliasing
import demo1 as m
print(m.x)
print(m.y)
m.add(20,30)
m.product(20,30)
