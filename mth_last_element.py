## mth_last_element.py
## Challenge # 10

import os

import sys

##with open(os.getcwd()+'\\mth_last_element_example.txt', 'r') as lines:
with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for test in testCases:
    test = test.split()
    if int(test[-1]) < len(test):
        print '{}'.format(test[ int(len(test)) - int(test[-1]) - 1 ])

