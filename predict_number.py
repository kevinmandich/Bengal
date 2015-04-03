## predict_number.py
## Challenge # 125

import os

import sys

with open(os.getcwd()+'\\predict_number_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

nums = {'0':'1', '1':'2', '2':'0'}

for k in testCases:

    k = int(k)
    a = 0
    while True:
        if 2**a - 1 >= k:
            break
        a += 1

    out = '0'
    print out

    for x in range(a):
        for char in out:
            out += nums[char]
        print out

    print ''




