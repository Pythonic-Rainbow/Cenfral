import datetime
import logging
import os

if not os.path.isdir("logs"):
    os.makedirs("logs")

time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
filename = 'logs\\' + time + '.log'
file = open(filename, 'w+')
file.close()
format = '%(asctime)s.%(msecs)d [%(name)s/%(levelname)s]: %(message)s'
logging.basicConfig(filename=filename,
                    filemode='a',
                    format=format,
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


class LogHandler:

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

    def info(self, msg: str):
        print(msg)
        self.logger.info(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)

    def warning(self, msg: str):
        print('WARNING:', msg)
        self.logger.warning(msg)

