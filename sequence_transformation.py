## sequence_transformation.py
## Challenge # 130

import os

import sys, time

with open(os.getcwd()+'\\sequence_transformation_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

def find_index(string, char):
    i = len(string)-1
    while i >= 0:
        if string[i] == char:
            return i
        i -= 1
    return 0

def can_transform(digs, chrs):

    ## check for easy cases
    if ((digs[0] == 0 and chrs[0] == 'B') or (digs[-1] == 0 and chrs[-1] == 'B')):
        print 'no 1'
        return 'No'
    if sum(digs) == 0:
        if 'B' not in chrs:
            return 'Yes'
    if 0 not in digs:
        if 'A' not in chrs:
            return 'Yes'
    if len(digs) == 1:
        if digs[0] == 0:
            if 'B' in chrs:
                print 'no 2'
                return 'No'
        if ('A' in chrs and 'B' in chrs):
            print 'no 3'
            return 'No'
            

    ## take care of A's first:
    i = 0
    chrIndex = 0 ## same as i, but for character list
    xformNum = 0
    #print 'i = {}'.format(i)
    while 0 in digs:
        if digs[i] == 0:
            numZero = 1
            while i+numZero < len(digs):
                if digs[i+numZero] == 0:
                    numZero += 1
                else:
                    break
            #print 'zeroIndex = {}'.format(i)
            #print 'numZero = {}'.format(numZero)

            if chrIndex >= len(chrs):
                #print chrIndex, len(chrs)
                #print 'index trouble'
                print 'no  - index trouble'
                return 'No'
            while chrs[chrIndex] != 'A':
                chrIndex += 1

            numChar = 1
            while chrIndex+numChar < len(chrs):
                if chrs[chrIndex+numChar] == 'A':
                    numChar += 1
                else:
                    break
            #print 'chrIndex = {}'.format(chrIndex)
            #print 'numChar = {}'.format(numChar)
            if numZero > numChar:
                print 'no - zero trouble'
                return 'No'
            

            for k in range(numZero):
                #print i, k
                digs[i+k] = '.'
            for k in range(numChar):
                chrs[chrIndex+k] = '.'
            chrIndex += numChar
            xformNum += 1
            i += 1
            #print '\n',digs
            #print chrs,'\n'
            #time.sleep(1)

        else:
            i += 1
            chrIndex += 1
            #print 'i = {}'.format(i)

    #print '\n',digs
    #print chrs,'\n'

    ## take care of B's next:
    i = 0
    chrIndex = 0
    while 1 in digs:
        if digs[i] == 1:
            numZero = 1
            while i+numZero < len(digs):
                if digs[i+numZero] == 1:
                    numZero += 1
                else:
                    break
            #print 'zeroIndex = {}'.format(i)
            #print 'numZero = {}'.format(numZero)

            while chrs[chrIndex] not in ['A','B']:
                chrIndex += 1

            numChar = 1
            while chrIndex+numChar < len(chrs):
                if chrs[chrIndex+numChar] in ['A','B']:
                    numChar += 1
                else:
                    break
            #print 'chrIndex = {}'.format(chrIndex)
            #print 'numChar = {}'.format(numChar)
            if numZero > numChar:
                print 'no - zero trouble 2nd'
                return 'No'


            for k in range(numZero):
                #print i, k
                digs[i+k] = 'X'
            for k in range(numChar):
                chrs[chrIndex+k] = 'X'
            chrIndex += numChar
            xformNum += 1
            i += 1
            #print '\n',digs
            #print chrs,'\n'

        else:
            i += 1
            chrIndex += 1

    if ('A' in chrs or 'B' in chrs):
        return 'No' 
    return 'Yes'

for line in testCases:
    #print line
    digs, chrs = line.split()
    chrs = list(chrs)
    digs = map(int, digs)

    #print digs
    #print chrs

    print can_transform(digs, chrs)
    #break




