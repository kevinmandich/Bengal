## minesweeper.py
## Challenge # 79

import os

import sys

with open(os.getcwd()+'\\minesweeper_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def find_adjacent(x, y, field):
    newField = [0 for i in range(len(field))]
    for i, c in enumerate(field):
        if c == '*':
            row, col = i/y, i%y
            for j in range(row-1, row+2):
                for k in range(col-1, col+2):
                    if not (j==row and k==col):
                        if (j >= 0 and j<x and k>=0 and k<y):
                            newField[j*y + k] += 1
    for i, c in enumerate(field):
        if c == '*':
            newField[i] = '*'
    return newField

for line in testCases:
    x, y = map(int, line.split(';')[0].split(','))
    field = line.split(';')[1]
    print ''.join(str(x) for x in find_adjacent(x, y, field))
