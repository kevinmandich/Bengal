## trailing_string.py
## Challenge # 32

import os

import sys

with open(os.getcwd()+'\\trailing_string_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    a, b = rec.split(',')[0], rec.split(',')[1]

    if b == a[-len(b):]:
        print 1
    else:
        print 0
