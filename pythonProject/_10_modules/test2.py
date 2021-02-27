# reloading a module:
# imp module:in python imp module is available
# reload() function: in imp module reload() function is available
from imp import reload
import module1
reload(module1)
reload(module1)
reload(module1)
reload(module1)
print("this is reload function")