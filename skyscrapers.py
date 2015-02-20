## skyscrapers.py
## Challenge # 120

import os

import sys

with open(os.getcwd()+'\\skyscrapers_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for bld in testCases:

    sky = {}
    sky[0] = 0
    for nums in bld.split(';'):
        nums = nums.strip('(').strip(')')
        low = int(nums.split(',')[0])
        height = int(nums.split(',')[1])
        high = int(nums.split(',')[2])

        for x in range(low, high+1):
            try:
                if height > sky[x]:
                    sky[x] = height
            except:
                sky[x] = height
        

