#!/usr/bin/python

from __future__ import division
import sys
import re

# map(int, sys.stdin.readline().split())

def isugly(x):
    return (x%2 == 0 or x%3 == 0 or x%5 == 0 or x%7 == 0)

#def myeval(x):
#    x = re.sub('(^|[+-])0(\d)', '\\1\\2', x)
#    return eval(x)

def place(s, zero=False):
    for i in xrange(1, len(s)):
        x = int(s[0:i])
        for part in place(s[i:]):
            yield x+part
            yield x-part
    yield int(s)

#ncases = int(sys.stdin.readline())
#for case in xrange(ncases):
#    s = sys.stdin.readline().split()[0]
s = '0000000000277'
count = 0
nums = []
for x in place(s):
    nums.append(x)
    count += isugly(x)

#for x in sorted(nums):
#    print x

print 'ugly = {}'.format(count)
