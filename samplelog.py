import logging

logging.basicConfig(filename='my_logs.log',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG)


logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")