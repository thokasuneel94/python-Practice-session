# if we are not specifying level then the default level is WARNING
# if we are not specifying file name,then the messages will be prionted to the console

# if we are not specifying level and specifying filename
import logging
logging.basicConfig(level=logging.WARNING)
print("logging started")
logging.debug("debug message")
logging.info("info message")
logging.error("error message")
logging.critical("critical message")
logging.warning("warning message")
print("logging ended")
