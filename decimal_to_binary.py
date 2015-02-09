## decimal_to_binary.py
## Challenge # 27

import os

import sys

with open(os.getcwd()+'\\decimal_to_binary_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    rec = bin(int(rec))[2:]
    print rec.lstrip('0')
