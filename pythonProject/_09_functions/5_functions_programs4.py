# generator functions:
# it is normal ordinary function, but in this yield keyword is used
# advantages:
# very easy to use
# memory utilization improved
# performance will be improved
# best suitable for reading data from large number of files
# web scraping and crawling
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# countdown the number by using generator
def countdown(num):
    print("start countdown")
    while num>0:
        yield num
        num=num-1
values=countdown(5)
for x in values:
    print(x)
# to generate first n numbers by using generator
def firstn(num):
    n=1
    while num>=n:
        yield n
        n=n+1
values=firstn(10)
for x in values:
    print(x)
# to generate fibonacci numbers upto 100 by using generator
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fib()
for x in f:
    if x>100:
        break
    print(x)
