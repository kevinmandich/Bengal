## interrupted_bubble_sort.py
## Challenge # 158

import os

import sys

with open(os.getcwd()+'\\interrupted_bubble_sort_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def bubble_sort(lst, currentItr):
    for i in range(len(lst)-1-currentItr):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return None

def partial_sort(lst, itr):
    if itr >= len(lst):
        itr = len(lst) - 1
    for x in range(itr):
        bubble_sort(lst, x)
    return lst


for text in testCases:
    lst = map(int, text.split('|')[0].split())
    itr = int(text.split('|')[1].strip())
    lst = partial_sort(lst, itr)
    print ' '.join(str(x) for x in lst)
