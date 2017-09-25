# put your python code here
import re
import sys

if __name__ == "__main__":
    data = sys.stdin.read()
    print(len(re.findall("you", data)))
