# garbage collection:
# to destroy useless objects and save the memory
# if an object does not have any reference variable,then that object is eligible for garbage collection
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

