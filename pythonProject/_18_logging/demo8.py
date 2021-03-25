# add timestamp in the log messages
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
print("logging started")
logging.debug("debug message")
logging.info("info message")
logging.error("error message")
logging.warning("warning message")
logging.critical("critical message")
print("logging ended")
