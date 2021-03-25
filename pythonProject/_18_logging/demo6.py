# how to format log messages:
# by using format keyword-argument,we can format messages

# to display only level name:
# logging.basicConfig(format='%(levelname)s')
import logging
logging.basicConfig(format='%(levelname)s')
print("logging started")
logging.debug("debug message")
logging.info("info message")
logging.error("error message")
logging.warning("warning message")
logging.critical("critical message")
print("logging ended")