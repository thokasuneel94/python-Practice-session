# transfer statements: break, continue, pass
# break:
for i in range(10):
    if i==7:
        print("processing is enough...plz break")
        break
    print(i)
cart=[10,20,600,60,70,90]
for item in cart:
    if item>500:
        print("sorry we cannot process this order...insurance must be required")
        break
    print("processing item:", item)
cart=[10,20,60,70,90]
for item in cart:
    if item>500:
        print("sorry we cannot process this item...,item,insurance must be required")
        break
    print("processing item:",item)
else:
    print("congrats...all items processed successfully")
cart=[10,20,600,60,70,90]
for item in cart:
    if item>550:
        print("sorry we cannot process this item...,item,insurance must be required")
        break
    print("processing item:",item)
else:
    print("congrats...all items processed successfully")
# continue:
for i in range(10):
    if i%2==0:
        continue
    print(i)
cart=[10,20,600,70,550,90]
for item in cart:
    if item>500:
        print("sorry we cannot process this item insurance must be requered")
        continue
    print("processing item:",item)
# pass:
def f1():
    print("hello")
def f2():
    print("hi")
print(f1())
print(f2())
def f1():
    print("hello")
def f2():
    pass
print(f1())
print(f2())
for i in range(100):
    if i%10==0:
        print(i)
    else:
        pass


