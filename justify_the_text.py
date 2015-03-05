## justify_the_text.py
## Challenge # 177

import os

import sys

with open(os.getcwd()+'\\justify_the_text_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:

    print text
