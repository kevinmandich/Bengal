## string_substitution.py
## Challenge # 50

import os

import sys

with open(os.getcwd()+'\\string_substitution_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for num in testCases:
    replacements = [[0],[1]]
    num, reps = num.split(';')
    num = map(int, num)
    reps = reps.split(',')
    for x in range(len(reps)/2):
        search, replace = map(int, list(reps[2*x])), map(int, list(reps[2*x+1]))
        i = 0
        while i + len(search) <= len(num):
            if search == num[i:i+len(search)]:
                replacements.append(replace)
                num[i:i+len(search)] = [len(replacements) - 1]
            i += 1
    final = ''
    for digit in num:
        final += ''.join(str(x) for x in replacements[digit])
    print final
