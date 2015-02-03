## multiples_of_a_number.py

import os

test_cases = open(os.getcwd()+'\\multiples_of_a_number_example.txt', 'r')

for test in test_cases:
    x, n = int(test.split(',')[0]), int(test.split(',')[1])
    multiple = 2
    while True:
        if n*multiple >= x:
            print n*multiple
            break
        else:
            multiple += 1
