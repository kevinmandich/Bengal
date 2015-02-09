## ugly_numbers.py
## Challenge # 42

import os

import sys

import itertools as it

with open(os.getcwd()+'\\ugly_numbers_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def is_ugly(x):
    return (x%2 == 0 or x%3 == 0 or x%5 == 0 or x%7 == 0)

def parse_expression(exp):
    num = 0
    for sub in exp.split('+'):
        if len(sub.split('-')) == 1:
            num += int(sub)
        else:
            num += int(sub.split('-')[0])
            for sub2 in sub.split('-')[1:]:
                num -= int(sub2)
    return num

operations = ['-','+','o']

for num in testCases:
    ugly = 0
    print 'number = {}'.format(num)
    #if num[0] == '0' and int(num) != 0:
    #    num = '0' + str(int(num))
    for combo in it.combinations_with_replacement(operations, len(num)-1):
        for perm in set(it.permutations(combo, len(num)-1)):
            number = num[0] + ''.join(perm[x-1] + num[x] for x in range(1, len(num)))
            number = parse_expression(''.join(c for c in number if c != 'o'))
            ugly += is_ugly(number)
    print ugly









