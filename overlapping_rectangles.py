## overlapping_rectangles.py
## Challenge # 70

import os

import sys

with open(os.getcwd()+'\\overlapping_rectangles_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    rec = [int(rec.split(',')[i]) for i in range(8)]
    if rec[6] < rec[0] or rec[4] > rec[2] or rec[7] > rec[1] or rec[5] < rec[3]:
        print 'False'
    else:
        print 'True'
