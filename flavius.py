## flavius.py
## Challenge # 71

import os

import sys

with open(os.getcwd()+'\\flavius_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:

    length, k = (int(x) for x in text.split(','))
    length -= 1

    nums = [x for x in range(length+1)]
    print nums

    result = ''
    i = k-1
    while len(nums) > 1:
        result += str(nums.pop(i%len(nums))) + ' '
        i += k - 1
        if i >= len(nums):
            i -= len(nums)

    result += str(nums[0])

    print result
