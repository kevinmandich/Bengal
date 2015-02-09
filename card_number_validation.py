## card_number_validation.py
## Challenge # 172

import os

import sys

with open(os.getcwd()+'\\card_number_validation_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    rec = [int(x) for x in ''.join(rec.split())][::-1]
    dig = 0
    for i, x in enumerate(rec):
        if i %2 == 0:
            dig += x
        else:
            new = 2 * x
            if new > 9:
                dig += sum(map(int, str(new)))
            else:
                dig += new
    if dig % 10 == 0:
        print 1
    else:
        print 0
