## string_permutations.py
## Challenge # 14

import os

import sys

with open(os.getcwd()+'\\string_permutations_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def find_perms(e):
    if len(e) <= 1:
        yield e
    else:
        for i in range(len(e)):
            for perm in find_perms(e[:i]+e[i+1:]):
                yield list(e[i]) + perm
            
for perms in testCases:
    perms = sorted(list(perms))
    perms = [x for x in find_perms(perms)]
    print ','.join(''.join(p) for p in perms)
