## fibonacci.py
## Challenge # 22

import os

import sys

with open(os.getcwd()+'\\fibonacci_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def fibonacci(num):

    if num == 0:
        return 0
    if num < 3:
        return 1

    a, b = 1, 1
    for x in range(num-2):
        a, b = b, a+b
    return b

for num in testCases:

    print fibonacci(int(num))
