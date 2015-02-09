## guess_number.py
## Challenge # 170

import os

import sys
import math

with open(os.getcwd()+'\\guess_number_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    rec = rec.split()
    high = int(rec[0])
    low = 0
    middle = 0
    for i in range(1, len(rec) - 1):
        middle = (low + high + 1)/2
        if rec[i] == 'Lower':
            high = middle - 1
        else:
            low = middle + 1
    print int((low + high + 1)/2)
