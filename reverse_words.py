## reverse_words.py

import os

test_cases = open(os.getcwd()+'\\reverse_words_sample.txt', 'r')

for test in test_cases:
    if len(test) < 2:
        continue
    print ' '.join(test.split()[::-1])
