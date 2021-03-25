# if we set level as WARNING.then it print only WARNING and higher-level messages will be written to the log file
import logging
logging.basicConfig(filename='demo1log.txt',level=logging.WARNING)
print("logging started")
logging.debug("debug message")
logging.error("error message")
logging.warning("warning message")
logging.critical("critical message")
logging.info("info message")
print("logging ended")
