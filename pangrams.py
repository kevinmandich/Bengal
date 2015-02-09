## pangrams.py
## Challenge # 37

import os

import sys, string

with open(os.getcwd()+'\\pangrams_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

alphabet = set(string.lowercase)
for rec in testCases:
    letters = set(''.join(rec.split()).lower())
    diff = alphabet - set(''.join(rec.split()).lower())
    if len(diff) > 0:
        print ''.join(sorted(diff))
    else:
        print 'NULL'
