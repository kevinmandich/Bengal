## simple_sorting.py
## Challenge # 22

import os

import sys

with open(os.getcwd()+'\\simple_sorting_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:

    nums = [float(x) for x in text.split()]
    nums.sort()
    print ' '.join('{0:.3f}'.format(x) for x in nums)
