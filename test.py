import sys

#sys.argv.pop(0) is test.py
if len(sys.argv) == 0:
    file = input('No file passed in. Please enter the path of original source code:')
