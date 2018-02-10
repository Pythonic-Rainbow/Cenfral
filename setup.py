from cenfral.log import LogHandler
import pip

setup = LogHandler('setup')
packages = ['fire']
for m in packages:
    setup.info('Verifying ' + m)
    pip.main(['install', m])
