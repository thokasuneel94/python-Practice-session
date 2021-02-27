# random module:
# to generate random numbers
# random numbers used in games
# in random module below functions are available
# random()
# randint()
# uniform
# randrange()
# choice() ....etc
import random

print(dir(random))
# random() function:
# in random module ramdom function is available
# random() function always generate some float values between 0 and 1 (not inclusive)
# 0<x<1
# syntax
from random import *

for i in range(10):
    print(random())

# randint() function:
# this function always generate some int values between any two numbers (inclusive)
# syntax
#
from random import *

for i in range(20):
    print(randint(1, 100))
#
from random import *

for i in range(20):
    print(randint(1, 10))
#   print(randint())      typeerror

# uniform() function:
# this function always generate some float values between any two numbers (not inclusive)
# syntax
from random import *

for i in range(20):
    print(uniform(1, 10))

# randrange() function:
# randrange(start,stop,step)
# start<=x<stop (start is inclusive and stop is not inclusive)
# start aurgument is optional and default value is 0
# step aurgument is optional and default value is 1
# randrange(10)===> generates a number from 0 to 9
# randrange(1,11)===>generates a number from 1 to 10
# randrange(1,11,2)===>generates a number 1,3,5,7,9
# syntax
#
from random import *

for i in range(10):
    print(randrange(10))
#
from random import *

for i in range(10):
    print(randrange(1, 11))
#
from random import *

for i in range(10):
    print(randrange(1, 11, 2))

# choice() function:
# it is don't return random number.it always return random object from the collection(list or tuple)
# syntax
#
from random import *

list = ["sunny", "bunny", "chinny", "vinny"]
for i in range(10):
    print(choice(list))

#
from random import *

list = ["sunny", "bunny", "chinny", "vinny"]
for i in range(10):
    print(choice("durga"))
#
from random import *
tuple = ("siva", "anil", "samantha", "kajal")
for i in range(10):
    print(choice(tuple))
# wap to generate a 6-digit random number as OTP
#
from random import *
for i in range(10):
    print(randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), sep='')
#   print(str(randrange)*6)
#
from random import *
for i in range(10):
    print(randint(100000,999999))
# wap to generate random pwd of 6 length 1,3,5 are alphabet symbols, 2,4,6 are digits
#
from random import *
for i in range(10):
    print(chr(randint(65,65+25)))    # A=65
#
from random import *
for i in range(10):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),sep='')



