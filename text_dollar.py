## text_dollar.py
## Challenge # 52

import os

import sys

with open(os.getcwd()+'\\text_dollar_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

tiers  = ['','Thousand','Million']
tens   = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
teens  = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
digits = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']


for num in testCases:
    number = 'Dollars'
    num = map(int, num)[::-1]
    for x in range((len(num)-1)/3+1):
        triple =  num[3*x:3*x+3]
        if sum(triple) > 0:
            number = tiers[x] + number
        for y in range(3 - len(triple)):
            triple.append(0)
        if triple[1] == 1 and triple[0] > 0:
            number = teens[triple[0]] + number
        elif triple[0] == 0:
            number = tens[triple[1]] + number
        else:
            number = digits[triple[0]] + number
            number = tens[triple[1]] + number
        if triple[2] > 0:
            number = digits[triple[2]] + 'Hundred' + number
    print number
