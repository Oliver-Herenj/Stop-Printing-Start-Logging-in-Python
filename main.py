import logging
import other_module

logging.basicConfig(
  format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
  datefmt='%d/%m/%Y %I:%M:%S %p',
  level=logging.DEBUG,
  filename='my_logs.log',
  filemode='w'
  )

logging.info('Hello, my name is Slim Shady!')
logging.warning('Oh no! You caught me!')


other_module.func()