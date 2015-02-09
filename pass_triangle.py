## pass_triangle.py
## Challenge # 89

import os

import sys

with open(os.getcwd()+'\\pass_triangle_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def find_max(tri):
    while len(tri) > 1:
        tri2 = tri.pop(-1)
        tri1 = tri.pop(-1)
        tri.append([max(tri2[x], tri2[x+1]) + tri1[x] for x in range(len(tri1))])
    return tri[0][0]

tri = []
for line in testCases:
    tri.append([int(x) for x in line.split()])

print find_max(tri)
