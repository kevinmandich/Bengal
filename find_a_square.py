## find_a_square.py
## Challenge # 101

import os

import sys

with open(os.getcwd()+'\\find_a_square_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def distance(vertex1, vertex2):

    return ( (vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)**0.5

for text in testCases:

    vertices = [x.lstrip('(').rstrip(')') for x in text.split(', ')]
    vertices = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in vertices]

    dist = []
    for v in vertices[1:]:

        dist.append(distance(vertices[0], v))

    dist.sort()

    if dist[0] == dist[1] == dist[2]:
        print 'false'
    elif dist[0] == dist[1] and abs(dist[0]*(2**0.5) - dist[2]) < 1e-4:
        print 'true'
    else:
        print 'false'

    print ''
