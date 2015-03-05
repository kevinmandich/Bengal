## hidden_digits.py
## Challenge # 122

import os

import sys

with open(os.getcwd()+'\\hidden_digits_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for text in testCases:

    result = ''

    for char in text:
        try:
            result += str(int(char))
        except:
            if 96 < ord(char) < 107:
                result += str(ord(char)-97)

    if len(result) > 0:
        print result
    else:
        print 'NONE'
