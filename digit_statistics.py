## digit_statistics.py
## Challenge # 144

import os

import sys

with open(os.getcwd()+'\\digit_statistics_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

patterns = [0,\
            0,\
            [2,4,8,6],\
            [3,9,7,1],\
            [4,6],\
            [5],\
            [6],
            [7,9,3,1],\
            [8,4,2,6],\
            [9,1]]


for num in testCases:
    digits = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    num, exp = map(int, num.split())
    numRepeats = exp/len(patterns[num])
    remainder = exp%len(patterns[num])
    for digit in patterns[num]:
        digits[digit] = numRepeats
    for x in range(remainder):
        digits[patterns[num][x]] += 1
    num = ''
    for x, y in digits.items():
        num += str(x)+': '+str(y)+', '
    print num.strip().strip(',')
