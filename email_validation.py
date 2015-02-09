## email_validation.py
## Challenge # 35

import os

import sys, re

with open(os.getcwd()+'\\email_validation_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    if len(re.findall(r'^[a-z|A-Z|0-9|_|-|+|.]+@[a-z|A-Z|0-9|_|-|+|.]+$|^".*"@[a-zA-Z0-9.+-_]+$', rec)) > 0:
        print 'true'
    else:
        print 'false'
