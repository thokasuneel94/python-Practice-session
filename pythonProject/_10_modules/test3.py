# reloading a module:
import time
from imp import reload
import module1
print("program entering into sleeping state")
time.sleep(30)
reload(module1)
print("program entering into sleeping state again")
time.sleep(30)
reload(module1)
print("this is last line of program")

