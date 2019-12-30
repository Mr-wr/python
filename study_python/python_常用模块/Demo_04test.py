import logging
logging.getLogger(__name__)
# #设置格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# #时间格式
DATE_FORMAT = "%m-%d-%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT,datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

# logging.warning("Some one delete the log file.", 
# exc_info=True, stack_info=True, 
# extra={'user': 'Tom', 'ip':'47.98.53.222'})