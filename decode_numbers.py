## decode_numbers.py
## Challenge # 73

import os

import sys

with open(os.getcwd()+'\\decode_numbers_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for test in testCases:
    num = len(test)
    for i in range(len(test) - 1):
        if test[i:i+2] > 0 and test[1:i+2] < 27:
            num += 1
    print num
