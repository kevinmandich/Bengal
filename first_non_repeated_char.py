## first_non_repeated_char.py
## Challenge # 12

import os

import sys

with open(os.getcwd()+'\\first_non_repeated_char_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    for i in range(len(rec)):
        prior = rec[:i]
        post  = rec[i+1:]
        if prior.find(rec[i]) == -1 and post.find(rec[i]) == -1:
            print rec[i]
            break
