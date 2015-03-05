## number_pairs.py
## Challenge # 34

import os

import sys

with open(os.getcwd()+'\\number_pairs_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:
    
    print text.lower()
