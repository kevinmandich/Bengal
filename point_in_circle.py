## point_in_circle.py
## Challenge # 98

import os

import sys, re

with open(os.getcwd()+'\\point_in_circle_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for rec in testCases:
    center = re.findall(r'Center:\s*\((.*?)\)', rec)[0]
    center = [float(num.strip()) for num in center.split(',')]
    radius = float(re.findall(r'Radius:\s*(.*?);', rec)[0])
    point = re.findall(r'Point:\s*\((.*?)\)$', rec)[0]
    point = [float(num.strip()) for num in point.split(',')]
    if ((center[0]-point[0])**2 + (center[1]-point[1])**2)**0.5 < radius:
        print 'true'
    else:
        print 'false'
