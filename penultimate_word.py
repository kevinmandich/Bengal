## penultimate_word.py
## Challenge # 92

import os

import sys

with open(os.getcwd()+'\\penultimate_word_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:
    
    print text.split()[-2]
