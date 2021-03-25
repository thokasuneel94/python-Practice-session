# to display levelname and message
# logging.basicConfig(format='%(levelname)s:%(message)s')
import logging
logging.basicConfig(format='%(levelname)s:%(message)s')
print("logging started")
logging.debug("debug message")
logging.error("error message")
logging.info("info message")
logging.warning("warning message")
logging.critical("critical message")
print("logging ended")
