## prefix_expressions.py
## Challenge # 7

import os

import sys

with open(os.getcwd()+'\\prefix_expressions_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def compute(string, x1, x2):

    if string == '*':
        return x1 * x2
    elif string == '+':
        return x1 + x2
    elif string == '/':
        return float(x1) / x2
            
for expr in testCases:

    expr = ''.join(x for x in expr.split())
    operations = expr[:len(expr)/2][::-1]
    nums = map(int, expr[len(expr)/2:])#[::-1]

    for op in operations:
        nums[1] = compute(op, nums[0], nums[1])
        nums.pop(0)

    print int(nums[0])

