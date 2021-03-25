# change date and time format
# we have to use special keyword argument: datefmt
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%y %I:%M:%S:%p')
# %I ====>means 12 hours' time scale
# %H ===>means 24 hours' time scale
# 12 hours time scale
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%y %I:%M:%S:%p')
print("logging started")
logging.debug("debug message")
logging.info("info message")
logging.error("error message")
logging.warning("warning message")
logging.critical("critical message")
print("logging ended")