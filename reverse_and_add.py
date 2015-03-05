## reverse_and_add.py
## Challenge # 45

import os

import sys

with open(os.getcwd()+'\\reverse_and_add_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def is_palindrome(number):

    if str(number) == str(number)[::-1]:
        return True
    return False

def add_reverse(number):

    return int(str(number)) + int(str(number)[::-1])

for num in testCases:

    num = int(num)
    n = 1
    while True:
        newNum = add_reverse(num)
        if is_palindrome(newNum):
            break
        num = newNum
        n += 1

    print str(n) + ' ' + str(newNum)
