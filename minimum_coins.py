## minimum_coins.py
## Challenge # 74

import os

import sys

with open(os.getcwd()+'\\minimum_coins_example.txt', 'r') as lines:
#with open(sys.argv[1], 'r') as lines:
    testCases = lines.read().splitlines()

for amount in testCases:
    amount = int(amount)
    coins = amount / 5
    amount -= coins*5
    coins += amount / 3
    amount -= 3*(amount / 3)
    coins += amount
    print coins
