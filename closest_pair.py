## closest_pair.py

import os

test_cases = open(os.getcwd()+'\\closest_pair_example.txt', 'r')

points = []
for test in test_cases:
    try:
        points.append((int(test.split()[0]), int(test.split()[1])))
    except:
        pass

dist = 10000
for i in range(len(points)):
    for j in range(i+1, len(points)):
        newDist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
        if newDist < dist:
            dist = newDist

if dist == 10000:
    print 'INFINITY'
else:
    print '{0:.4f}'.format(dist)
