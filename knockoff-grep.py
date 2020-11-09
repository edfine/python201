import sys
import re

if len(sys.argv) < 3:
    print('usage: {} filename pattern'.format(sys.argv[0]))
    sys.exit(1)

try:
    cre = re.compile(sys.argv[2])
except:
    print('bogus re')
    sys.exit(1)

try:
    for line in open(sys.argv[1]):
        if re.search(cre, line):
            print(line, end='')
except (FileNotFoundError, PermissionError):
    print("Can't open", sys.argv[1])
