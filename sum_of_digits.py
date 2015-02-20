## sum_of_digits.py
## Challenge # 21

import os

import sys

with open(os.getcwd()+'\\sum_of_digits_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def sum_digits(num):

    sum_ = 0
    while num:
        sum_, num = sum_ + num%10, num/10
    return sum_

for num in testCases:
    
    print sum_digits(int(num))
