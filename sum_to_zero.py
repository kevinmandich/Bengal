## sum_to_zero.py
## Challenge # 81

import os

import sys, itertools

with open(os.getcwd()+'\\sum_to_zero_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    rec = [int(x) for x in rec.split(',')]
    total = 0
    for combo in itertools.combinations(rec, 4):
        if sum(combo) == 0:
            total += 1
    print total
