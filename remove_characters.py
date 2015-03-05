## remove_characters.py
## Challenge # 13

import os

import sys

with open(os.getcwd()+'\\remove_characters_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for case in testCases:

    test = case.split(',')[0]
    chars = case.split(',')[1].strip()

    for char in chars:
        test = test.replace(char, '')

    print test
