# inside of module members also have aliasing:
from demo1 import x as c,y as d,add as sum,product as multi
print(c)
print(d)
sum(50,70)
multi(50,70)