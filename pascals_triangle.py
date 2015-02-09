## pascals_triangle.py
## Challenge # 66

import os

import sys

with open(os.getcwd()+'\\pascals_triangle_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    rec = int(rec)
    if rec == 1:
        print rec
        continue
    depth = 1
    nums = [1]
    for i in range(1, rec):
        depth += 1
        nums.append(1)
        for j in range(2,depth):
            nums.append(nums[len(nums)-depth] + nums[len(nums)-depth+1])
        nums.append(1)
    for num in nums:
        print num,
    print ''
