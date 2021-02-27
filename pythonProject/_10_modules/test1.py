# import module many times, but loaded only one time
import module1
import module1
import module1
import module1
import module1
import module1
print("this is test module")
#
import time
import module1
print("program entering into sleeping state")
time.sleep(30)
import module1
print("this is last line of program")