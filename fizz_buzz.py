## fizz_buzz.py
## Challenge # 1

import os

import sys

with open(os.getcwd()+'\\fizz_buzz_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:
    
    a, b, c = (int(x) for x in text.split())

    seq = ''
    for num in range(1,c+1):

        if num % a == 0:
            if num % b == 0:
                seq += 'FB '
            else:
                seq += 'F '
        elif num %b == 0:
            seq += 'B '
        else:
            seq += str(num) + ' '

    print seq.strip()
