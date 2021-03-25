# writing python program exceptions to the log file
# logging.exception(msg)
import logging
logging.basicConfig(filename='demo11log.txt',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%y %I:%M:%S:%p')
print("logging started")
logging.info("a new request came")
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except ZeroDivisionError as msg:
    print("cannot divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("please provide int values only")
    logging.exception(msg)
logging.info("request processing completed")

