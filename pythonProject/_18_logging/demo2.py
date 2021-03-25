# if we set level as DEBUG then all messages will be written to the log file
import logging
logging.basicConfig(filename='demo2log.txt',level=logging.DEBUG)
print("logging started")
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.critical("critical message")
logging.error("error message")
print("logging end")