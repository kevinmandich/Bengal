## sum_integers.py
## Challenge # 24

import sys

with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().strip().splitlines()

print sum((int(test) for test in testCases))
