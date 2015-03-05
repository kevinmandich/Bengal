## delta_time.py

import os

test_cases = open(os.getcwd()+'\\delta_time_example.txt', 'r')

for test in test_cases:
    t1, t2 = test.split()[0], test.split()[1]
    t1 = int(t1.split(':')[0])*3600 + int(t1.split(':')[1])*60 + int(t1.split(':')[2])
    t2 = int(t2.split(':')[0])*3600 + int(t2.split(':')[1])*60 + int(t2.split(':')[2])
    t1 = abs(t1-t2)

    hours = t1/3600
    minutes = (t1 - hours*3600)/60
    seconds = t1 - hours*3600 - minutes*60

    hours = str(hours)
    if len(hours) == 1:
        hours = '0'+hours
    minutes = str(minutes)
    if len(minutes) == 1:
        minutes = '0'+minutes
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = '0'+seconds
    
    print hours+':'+minutes+':'+seconds

