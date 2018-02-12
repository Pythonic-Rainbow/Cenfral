import configparser
import datetime
import logging
import os

time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
filename = 'logs\\' + time + '.log'
format = '%(asctime)s.%(msecs)d [%(name)s/%(levelname)s]: %(message)s'
fdir = os.path.dirname(os.path.dirname(__file__)) + '\\cenfral.cfg'
cg = configparser.ConfigParser()
if not os.path.isfile(fdir):
    cg['General'] = {'saveLogs': 'True'}
    with open(fdir, 'w') as configfile:
        cg.write(configfile)

rg = configparser.ConfigParser()
rg.read(fdir)
if rg['General']['saveLogs'] == 'True':
    if not os.path.isdir("logs"):
        os.makedirs("logs")
    file = open(filename, 'w+')
    file.close()
    logging.basicConfig(filename=filename,
                        filemode='a',
                        format=format,
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)


def fexists():
    if os.path.isfile(filename):
        return True
    else:
        return False


class LogHandler:

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

    def info(self, msg: str):
        print(msg)
        self.logger.info(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)

    def warning(self, msg: str):
        if fexists():
            print('WARNING: ' + msg)
        self.logger.warning(msg)
