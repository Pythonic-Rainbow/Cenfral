import configparser
import os.path
from cenfral.log import LogHandler

cfglog = LogHandler('config')


def write(cofg):
    with open(fdir, 'w') as configfile:
        cfglog.debug('Writing config')
        cofg.write(configfile)


cfg = configparser.ConfigParser()
fdir = os.path.dirname(os.path.dirname(__file__)) + '\\cenfral.cfg'


def read():
    cfglog.debug('Reading config')
    return cfg.read(fdir)


def update(sec: str, key: str, value: object):
    config = read()
    if config[sec][key] != value:
        cfglog.debug('Updating config')
        config[sec][key] = value
    write(config)
