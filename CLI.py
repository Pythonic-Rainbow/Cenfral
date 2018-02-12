import sys

import fire

from cenfral.log import LogHandler

CLI = LogHandler('CLI')


def noarg():
    CLI.warning('No program arguments passed.While this is not a fatal problem,it is recommended that you use Cenfral '
                'with `python cenfral.py <args>` !\nAlternatively you can drag and drop the file to cenfral.py!')


if __name__ == '__main__':
    CLI.debug('Script called')
    cla = sys.argv[1:]
    if len(cla) == 0:
        fire.Fire(noarg)
