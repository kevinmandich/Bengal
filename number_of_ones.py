## mth_last_element.py
## Challenge # 16

import os, sys, time

with open(os.getcwd()+'\\number_of_ones_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

t1 = time.time()

for test in testCases:
    a = bin(int(test))[2:]
    print a.count('1')

t2 = time.time()
print 'time = {} seconds'.format(t2-t1)
