import sys

try:
    arg = sys.argv[1]
    num = int(arg)

except(IndexError, ValueError):
    exit('Please enter an integer on the command line')
