## string_list.py
## Challenge #38

import os
import itertools as it

with open(os.getcwd()+'\\string_list_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for test in testCases:

    n = int(test.split(',')[0])
    text = list(test.split(',')[1])

    text = sorted(list(set(it.product(text, repeat=n))))

    toPrint = ''
    for x in text:
        for y in x:
            toPrint += y
        toPrint += ','

    print toPrint.strip(',')
