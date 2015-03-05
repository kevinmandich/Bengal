## reverse_groups.py
## Challenge # 71

import os

import sys

with open(os.getcwd()+'\\reverse_groups_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:

    nums = text.split(';')[0]
    k = int(text.split(';')[1])

    nums = [x for x in nums.split(',')]

    for i in range(len(nums)/k):
        nums[i*k:i*k+k] = nums[i*k:i*k+k][::-1]

    out = ''
    for num in nums:
        out += num + ','

    print out.rstrip(',')
